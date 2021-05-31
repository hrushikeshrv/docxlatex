import zipfile
from defusedxml import ElementTree

from tagparsers import tag_to_latex, qn


class Document:
    def __init__(self, document, inline_delimiter='$', block_delimiter='$$', get_header=False, get_footer=False):
        self.document = document
        self.inline_delimiter = inline_delimiter
        self.block_delimiter = block_delimiter
        self.get_header_text = get_header
        self.get_footer_text = get_footer
    
    def get_text(self, get_header_text=False, get_footer_text=False):
        """
        Extract the text from the .docx file while converting the equations in the document
        to valid LaTeX syntax, enclosed within the specified delimiters
        
        :param get_header_text:bool - True if you want to extract text from the header, False otherwise
        :param get_footer_text:bool - True if you want to extract text from the footer, False otherwise
        :return text:str - The extracted text
        """
        zip_f = zipfile.ZipFile(self.document)
        text = ''
        for f in zip_f.namelist():
            if get_header_text and f.startswith('word/header'):
                text += self.xml_to_text(zip_f.read(f))
            if f.startswith('word/document'):
                text += self.xml_to_text(zip_f.read(f))
            if get_footer_text and f.startswith('word/footer'):
                text += self.xml_to_text(zip_f.read(f))
        
        zip_f.close()
        return text

    def xml_to_text(self, xml):
        """
            Recursively iterate over the ElementTree of the word document and extract text content from supported tags.

            :param xml:str - XML string to be parsed into an xml.etree.Element object.
            :return text:str - The text contained in the tag

            TODO -
                1. Check for newlines before and after equation and switch to block_delimiter accordingly
            """
        text = ''
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
        
            elif child.tag == qn('w:tab'):
                text += '\t'
            elif child.tag == qn('w:br') or child.tag == qn('w:cr'):
                text += '\n'
            elif child.tag == qn('w:p'):
                text += '\n\n'
    
        return text
