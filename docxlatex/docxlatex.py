import zipfile
from defusedxml import ElementTree
import re
import os

from .tagparsers import tag_to_latex, qn


class Document:
    def __init__(self, document, inline_delimiter='$', block_delimiter='$$'):
        self.document = document
        self.inline_delimiter = inline_delimiter
        self.block_delimiter = block_delimiter
    
    def get_text(self, get_header_text=False, get_footer_text=False, image_dir=None, extensions=None):
        """
        Extract the text from the .docx file while converting the equations in the document
        to valid LaTeX syntax, enclosed within the specified delimiters
        
        :param get_header_text:bool - True if you want to extract text from the header, False otherwise
        :param get_footer_text:bool - True if you want to extract text from the footer, False otherwise
        :param image_dir:str - The path to the directory where you want to store images
        :param extensions:List[str], tuple - A list of tuple of string of the extensions you want to extract (['.jpg', '.png', ...])
        :return text:str - The extracted text
        """
        if extensions is None:
            extensions = ['.jpg', '.jpeg', '.png', '.svg', '.bmp', '.gif']
        zip_f = zipfile.ZipFile(self.document)
        text = ''
        for f in zip_f.namelist():
            if get_header_text and f.startswith('word/header'):
                text += self.xml_to_text(zip_f.read(f))
            if f.startswith('word/document'):
                text += self.xml_to_text(zip_f.read(f))
            if get_footer_text and f.startswith('word/footer'):
                text += self.xml_to_text(zip_f.read(f))
        
        if image_dir is not None:
            for f in zip_f.namelist():
                _, extension = os.path.splitext(f)
                if extension in extensions:
                    destination = os.path.join(image_dir, os.path.basename(f))
                    with open(destination, 'wb') as destination_file:
                        destination_file.write(zip_f.read(f))
        zip_f.close()
        return text

    def xml_to_text(self, xml):
        """
            Recursively iterate over the ElementTree of the word document and extract text content from supported tags.

            :param xml:str - XML string to be parsed into an xml.etree.Element object.
            :return text:str - The text contained in the tag
            """
        text = ''
        n_images = 0
        root = ElementTree.fromstring(xml)
        for child in root.iter():
            if child.get('docxlatex_skip_iteration', False):
                continue
        
            if child.tag == qn('w:t'):
                text += child.text if child.text is not None else ''
            elif child.tag == qn('m:oMath'):
                text += self.inline_delimiter + ' '
                text += tag_to_latex(child)
                text += ' ' + self.inline_delimiter
            elif child.tag == qn('m:r'):
                text += ''.join(child.itertext())
            elif child.tag == qn('w:drawing'):
                n_images += 1
                text += f'\nIMAGE#{n_images}-image{n_images}\n'
        
            elif child.tag == qn('w:tab'):
                text += '\t'
            elif child.tag == qn('w:br') or child.tag == qn('w:cr'):
                text += '\n'
            elif child.tag == qn('w:p'):
                text += '\n\n'
        
        text = re.sub(r'\n(\n+)\$(\s*.+\s*)\$\n', r'\n\1$$ \2 $$', text)
        return text
