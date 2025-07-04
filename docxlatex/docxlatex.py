import zipfile
from defusedxml import ElementTree
from xml.dom import minidom
import re
import os

from docxlatex.parser.utils import linear_expression, qn
from docxlatex.parser import OMMLParser


class Document:
    def __init__(self, document, inline_delimiter="$", block_delimiter="$$"):
        self.document = document
        self.inline_delimiter = inline_delimiter
        self.block_delimiter = block_delimiter
        self.equations = []

    def get_text(
        self,
        linear_format: bool = False,
        get_header_text: bool = False,
        get_footer_text: bool = False,
        image_dir: str | None = None,
        image_extensions: list[str] | tuple[str] | None = None,
    ):
        """
        Extract the text from the .docx file while converting the equations in the document
        to valid LaTeX syntax, enclosed within the specified delimiters

        :param linear_format:bool - True if the inserted equations in the document have been converted
            into linear format in LaTeX syntax, False if the equations are in professional formatting.
            We assume the equations are not in Unicode or any other format. Defaults to False.
        :param get_header_text:bool - True if you want to extract text from the header, False otherwise
        :param get_footer_text:bool - True if you want to extract text from the footer, False otherwise
        :param image_dir:str - The path to the directory where you want to store images
        :param image_extensions:List[str], tuple - A list or tuple of strings of the extensions you want to
            extract (['.jpg', '.png', ...])
        :return text:str - The extracted text
        """
        if image_extensions is None:
            image_extensions = [".jpg", ".jpeg", ".png", ".svg", ".bmp", ".gif"]
        zip_f = zipfile.ZipFile(self.document)
        text = ""
        for f in zip_f.namelist():
            if get_header_text and f.startswith("word/header"):
                text += self.xml_to_text(zip_f.read(f), linear_format)
            if f.startswith("word/document"):
                text += self.xml_to_text(zip_f.read(f), linear_format)
            if get_footer_text and f.startswith("word/footer"):
                text += self.xml_to_text(zip_f.read(f), linear_format)

        if image_dir is not None:
            for f in zip_f.namelist():
                _, extension = os.path.splitext(f)
                if extension in image_extensions:
                    destination = os.path.join(image_dir, os.path.basename(f))
                    with open(destination, "wb") as destination_file:
                        destination_file.write(zip_f.read(f))
        zip_f.close()
        return text

    def get_xml(self):
        """
        :return: The XML representation of the document body (ignores the header and footer)
        """
        _xml = ""
        zip_f = zipfile.ZipFile(self.document)
        for f in zip_f.namelist():
            if f.startswith("word/document"):
                dom = minidom.parse(zip_f.open(f))
                _xml = dom.toprettyxml()
                break
        zip_f.close()
        return _xml

    def pprint_xml(self):
        zip_f = zipfile.ZipFile(self.document)
        for f in zip_f.namelist():
            if f.startswith("word/document"):
                dom = minidom.parse(zip_f.open(f))
                print(dom.toprettyxml())
                break
        zip_f.close()

    def xml_to_text(self, xml: bytes, linear_format: bool) -> str:
        """
        Recursively iterate over the ElementTree of the document and extract text content from supported tags.

        :param xml:str - XML string to be parsed into an xml.etree.Element object.
        :param linear_format:bool - True if the equations in the document have been converted into
        linear format in LaTeX syntax. False if the equations are in professional formatting.
        We assume the equations are not in Unicode or any other format.
        :return text:str - The text contained in the tag
        """
        text = ""
        n_images = 0
        root = ElementTree.fromstring(xml)
        for child in root.iter():
            if child.get("docxlatex_skip_iteration", False):
                continue

            # Found text
            if child.tag == qn("w:t"):
                text += child.text if child.text is not None else ""

            # Found an equation
            elif child.tag == qn("m:oMath"):
                if linear_format:
                    eqn = linear_expression(child)
                    text += self.inline_delimiter + " "
                    text += eqn
                    text += " " + self.inline_delimiter
                    self.equations.append(eqn)
                else:
                    eqn = OMMLParser().parse(child)
                    text += (
                        f"{self.inline_delimiter} " + eqn + f" {self.inline_delimiter}"
                    )
                    self.equations.append(eqn)
            elif child.tag == qn("m:r") and linear_format:
                text += "".join(child.itertext())

            # Found an image
            elif child.tag == qn("w:drawing"):
                n_images += 1
                text += f"\nIMAGE#{n_images}-image{n_images}\n"

            elif child.tag == qn("w:tab"):
                text += "\t"
            elif child.tag == qn("w:br") or child.tag == qn("w:cr"):
                text += "\n"
            elif child.tag == qn("w:p"):
                text += "\n\n"

        text = re.sub(
            rf"\n(\n+){self.inline_delimiter}(\s*.+\s*){self.inline_delimiter}\n",
            rf"\n\1{self.block_delimiter} \2 {self.block_delimiter}",
            text,
        )
        return text
