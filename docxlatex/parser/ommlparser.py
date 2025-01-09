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
            768: '\\grave',
            769: '\\acute',
            770: '\\hat',
            771: '\\tilde',
            773: '\\bar',
            774: '\\breve',
            775: '\\dot',
            776: '\\ddot',
            780: '\\check',
            831: '\\overline{\\overline',
            8400: '\\overset\\leftharpoonup',
            8401: '\\overset\\rightharpoonup',
            8406: '\\overleftarrow',
            8407: '\\overrightarrow',
            8411: '\\dddot',
            8417: '\\overset\\leftrightarrow',
        }
        text = ''
        accent = 770
        for child in root:
            if child.tag == qn('m:accPr'):
                for child2 in child:
                    if child2.tag == qn('m:chr'):
                        accent = ord(child2.attrib.get(qn('m:val')))

        text += character_map[accent] + '{'
        for child in root:
            if child.tag == qn('m:e'):
                text += self.parse(child)
        text += '}'
        if accent == 831:
            text += '}'
        return text

    def parse_bar(self, root: Element) -> str:
        text = '\\overline{'
        for child in root:
            if child.tag == qn('m:barPr'):
                for child2 in child:
                    if child2.tag == qn('m:pos'):
                        if child2.attrib.get(qn('m:val')) == 'bot':
                            text = '\\underline{'

        for child in root:
            if child.tag == qn('m:e'):
                text += self.parse(child)
        text += '}'
        return text

    def parse_border_box(self, root: Element) -> str:
        text = '\\boxed{'
        for child in root:
            if child.tag == qn('m:e'):
                text += self.parse(child)
        text += '}'
        return text

    def parse_group_chr(self, root: Element) -> str:
        text = '\\underbrace{'
        for child in root:
            if child.tag == qn('m:groupChrPr'):
                for child2 in child:
                    if child2.tag == qn('m:pos') and child2.attrib.get(qn('m:val')) == 'top':
                        text = '\\overbrace{'
        for child in root:
            if child.tag == qn('m:e'):
                text += self.parse(child)
        text += '}'
        return text

    def parse_f(self, root: Element) -> str:
        text = '\\frac{'
        for child in root:
            if child.tag == qn('m:num'):
                text += self.parse(child)
        text += '}{'
        for child in root:
            if child.tag == qn('m:den'):
                text += self.parse(child)
        text += '}'
        return text

    parsers = {
        qn('m:r'): parse_r,
        qn('m:acc'): parse_acc,
        qn('m:borderBox'): parse_border_box,
        qn('m:bar'): parse_bar,
        qn('m:groupChr'): parse_group_chr,
        qn('m:f'): parse_f,
    }
