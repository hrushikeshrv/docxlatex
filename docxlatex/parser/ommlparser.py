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
                text += self.parsers[child.tag](self, child)
        return text

    def parse_acc(self, root: Element) -> str:
        character_map = {
            '&#768;': '\\grave',
            '&#769;': '\\acute',
            '&#770;': '\\hat',
            '&#771;': '\\tilde',
            '&#773;': '\\bar',
            '&#774;': '\\breve',
            '&#775;': '\\dot',
            '&#776;': '\\ddot',
            '&#780;': '\\check'
        }
        text = ''
        accent = '&#770;'
        for child in root:
            if child.tag == qn('m:accPr'):
                for child2 in child:
                    if child2.tag == qn('m:chr'):
                        accent = child2.attrib.get('m:val')

        text += character_map[accent] + '{'
        for child in root:
            if child.tag == qn('m:e'):
                for child2 in child:
                    if child2.tag in self.parsers:
                        text += self.parsers[child2.tag](self, child2)
        text += '}'
        return text

    parsers = {
        qn('m:r'): parse_r,
        qn('m:acc'): parse_acc,
    }
