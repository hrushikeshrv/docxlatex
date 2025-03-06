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
        text = ""
        for child in root:
            if child.tag in self.parsers:
                text += self.parsers[child.tag](self, child)
        return text

    def parse_r(self, root: Element) -> str:
        text = ""
        for child in root:
            if child.tag == qn("m:t"):
                text += "".join(child.itertext())
            elif child.tag in self.parsers:
                text += self.parsers[child.tag](self, child)
        return text

    def parse_acc(self, root: Element) -> str:
        character_map = {
            768: "\\grave",
            769: "\\acute",
            770: "\\hat",
            771: "\\tilde",
            773: "\\bar",
            774: "\\breve",
            775: "\\dot",
            776: "\\ddot",
            780: "\\check",
            831: "\\overline{\\overline",
            8400: "\\overset\\leftharpoonup",
            8401: "\\overset\\rightharpoonup",
            8406: "\\overleftarrow",
            8407: "\\overrightarrow",
            8411: "\\dddot",
            8417: "\\overset\\leftrightarrow",
        }
        text = ""
        accent = 770
        for child in root:
            if child.tag == qn("m:accPr"):
                for child2 in child:
                    if child2.tag == qn("m:chr"):
                        accent = ord(child2.attrib.get(qn("m:val")))

        text += character_map[accent] + "{"
        for child in root:
            if child.tag == qn("m:e"):
                text += self.parse(child)
        text += "}"
        if accent == 831:
            text += "}"
        return text

    def parse_bar(self, root: Element) -> str:
        text = "\\overline{"
        for child in root:
            if child.tag == qn("m:barPr"):
                for child2 in child:
                    if child2.tag == qn("m:pos"):
                        if child2.attrib.get(qn("m:val")) == "bot":
                            text = "\\underline{"

        for child in root:
            if child.tag == qn("m:e"):
                text += self.parse(child)
        text += "}"
        return text

    def parse_border_box(self, root: Element) -> str:
        text = "\\boxed{"
        for child in root:
            if child.tag == qn("m:e"):
                text += self.parse(child)
        text += "}"
        return text

    def parse_group_chr(self, root: Element) -> str:
        text = "\\underbrace{"
        for child in root:
            if child.tag == qn("m:groupChrPr"):
                for child2 in child:
                    if (
                        child2.tag == qn("m:pos")
                        and child2.attrib.get(qn("m:val")) == "top"
                    ):
                        text = "\\overbrace{"
        for child in root:
            if child.tag == qn("m:e"):
                text += self.parse(child)
        text += "}"
        return text

    def parse_d(self, root: Element) -> str:
        bracket_map = {
            "(": "\\left(",
            ")": "\\right)",
            "[": "\\left[",
            "]": "\\right]",
            "{": "\\left{",
            "}": "\\right}",
            "〈": "\\left\\langle",
            "〉": "\\right\\rangle",
            "⌊": "\\left\\lfloor",
            "⌋": "\\right\\rfloor",
            "⌈": "\\left\\lceil",
            "⌉": "\\right\\rceil",
            "|": "\\left|",
            "‖": "\\left\\|",
        }
        text = ""
        start_bracket = "("
        end_bracket = ")"
        seperator = "|"
        for child in root:
            if child.tag == qn("m:dPr"):
                for child2 in child:
                    if child2.tag == qn("m:begChr"):
                        start_bracket = child2.attrib.get(qn("m:val"))
                    if child2.tag == qn("m:endChr"):
                        end_bracket = child2.attrib.get(qn("m:val"))
                    if child2.tag == qn("m:sepChr"):
                        seperator = child2.attrib.get(qn("m:val"))
        for child in root:
            if child.tag == qn("m:e"):
                if text:
                    text += seperator
                text += self.parse(child)
        if start_bracket and end_bracket:
            if end_bracket == "|":
                text = bracket_map[start_bracket] + " " + text + " " + "\\right|"
            elif end_bracket == "‖":
                text = bracket_map[start_bracket] + " " + text + " " + "\\right\\|"
            else:
                text = (
                    bracket_map[start_bracket]
                    + " "
                    + text
                    + " "
                    + bracket_map[end_bracket]
                )
        return text

    def parse_f(self, root: Element) -> str:
        text = "\\frac{"
        for child in root:
            if child.tag == qn("m:num"):
                text += self.parse(child)
        text += "}{"
        for child in root:
            if child.tag == qn("m:den"):
                text += self.parse(child)
        text += "}"
        return text

    def parse_s_sup(self, root: Element) -> str:
        content = ""
        exp_content = ""
        for child in root:
            if child.tag == qn("m:e"):
                content = self.parse(child)
            if child.tag == qn("m:sup"):
                exp_content = self.parse(child)
        return f"{{{content}}}^{{{exp_content}}}"

    def parse_s_sub(self, root: Element) -> str:
        content = ""
        sub_content = ""
        for child in root:
            if child.tag == qn("m:e"):
                content = self.parse(child)
            if child.tag == qn("m:sub"):
                sub_content = self.parse(child)
        return f"{{{content}}}_{{{sub_content}}}"

    def parse_s_sub_sup(self, root: Element) -> str:
        content = ""
        sub_content = ""
        exp_content = ""
        for child in root:
            if child.tag == qn("m:e"):
                content = self.parse(child)
            if child.tag == qn("m:sub"):
                sub_content = self.parse(child)
            if child.tag == qn("m:sup"):
                exp_content = self.parse(child)
        return f"{{{content}}}_{{{sub_content}}}^{{{exp_content}}}"

    def parse_s_pre(self, root: Element) -> str:
        content = ""
        sub_content = ""
        exp_content = ""
        for child in root:
            if child.tag == qn("m:e"):
                content = self.parse(child)
            if child.tag == qn("m:sub"):
                sub_content = self.parse(child)
            if child.tag == qn("m:sup"):
                exp_content = self.parse(child)
        return "{}^{" + exp_content + "}_{" + sub_content + "}{" + content + "}"

    def parse_rad(self, root: Element) -> str:
        content = ""
        order = ""
        for child in root:
            if child.tag == qn("m:deg"):
                order = self.parse(child)
            if child.tag == qn("m:e"):
                content += self.parse(child)
        if order:
            return f"\\sqrt[{order}]{{{content}}}"
        return f"\\sqrt{{{content}}}"

    def parse_nary(self, root: Element) -> str:
        character_map = {
            8719: "\\prod",
            8720: "\\coprod",
            8721: "\\sum",
            8747: "\\int",
            8748: "\\iint",
            8749: "\\iiint",
            8750: "\\oint",
            8751: "\\oiint",
            8752: "\\oiiint",
            8896: "\\bigwedge",
            8897: "\\bigvee",
            8898: "\\bigcap",
            8899: "\\bigcup",
        }
        char = 8747
        for child in root:
            if child.tag == qn("m:naryPr"):
                for child2 in child:
                    if child2.tag == qn("m:chr"):
                        char = ord(child2.attrib.get(qn("m:val")))
        text = character_map.get(char, character_map[8721])
        sub = ""
        sup = ""
        content = ""
        for child in root:
            if child.tag == qn("m:sub"):
                sub = self.parse(child)
            if child.tag == qn("m:sup"):
                sup = self.parse(child)
            if child.tag == qn("m:e"):
                content = self.parse(child)
        if sub:
            text += f"_{{{sub}}}"
        if sup:
            text += f"^{{{sup}}}"
        text += "{" + content + "}"
        return text

    parsers = {
        qn("m:r"): parse_r,
        qn("m:acc"): parse_acc,
        qn("m:borderBox"): parse_border_box,
        qn("m:bar"): parse_bar,
        qn("m:d"): parse_d,
        qn("m:groupChr"): parse_group_chr,
        qn("m:f"): parse_f,
        qn("m:sSup"): parse_s_sup,
        qn("m:sSub"): parse_s_sub,
        qn("m:sSubSup"): parse_s_sub_sup,
        qn("m:sPre"): parse_s_pre,
        qn("m:rad"): parse_rad,
        qn("m:nary"): parse_nary,
    }
