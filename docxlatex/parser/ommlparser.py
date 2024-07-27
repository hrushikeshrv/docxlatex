from xml.dom.minidom import Element

from docxlatex.parser.utils import qn


class OMMLParser:
    """
    Parser class for reading OMML and converting it into LaTeX.
    """
    def parse(self, root: Element) -> str:
        """
        Parses an m:oMath OMML tag into LaTeX.
        :param root: An m:oMath OMML tag
        :return: The LaTeX representation of the OMML input
        """
        text = ''
        for child in root:
            if child.tag in self.parsers:
                text += self.parsers[child.tag](self, child)
        return text

    def parse_r(self, root: Element) -> str:
        text = ''
        for child in root:
            if child.tag == qn('m:t'):
                text += ''.join(child.itertext())
            elif child.tag in self.parsers:
                text += self.parsers[child.tag](child)
        return text

    parsers = {
        qn('m:r'): parse_r
    }
