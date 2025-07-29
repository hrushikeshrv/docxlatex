from xml.etree.cElementTree import Element

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
        if root.tag == qn("m:t"):
            return self.parse_t(root)
        for child in root:
            if child.tag in self.parsers:
                text += self.parsers[child.tag](self, child)
        return text

    def parse_e(self, root: Element) -> str:
        text = ""
        for child in root:
            text += self.parse(child)
        return text

    def parse_r(self, root: Element) -> str:
        # TODO: Add support for m:rPr and m:scr to support different character styles
        #    For now, we just parse the text content of m:r
        text = ""
        for child in root:
            text += self.parse(child)
        return text

    def parse_t(self, root: Element):
        symbol_map = {
            "≜": "\\triangleq",
            "≝": "\\stackrel{\\tiny def}{=}",
            "≞": "\\stackrel{\\tiny m}{=}",
        }
        text = root.text.split()
        if not text:
            return " "
        for i, t in enumerate(text):
            if t in symbol_map:
                text[i] = symbol_map[t]
        return " ".join(text)

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

    def parse_box(self, root: Element) -> str:
        text = ""
        for child in root:
            text += self.parse(child)
        return text

    def parse_group_chr(self, root: Element) -> str:
        character_map = {
            "←": "\\leftarrow",
            "→": "\\rightarrow",
            "↔": "\\leftrightarrow",
            "⇐": "\\Leftarrow",
            "⇒": "\\Rightarrow",
            "⇔": "\\Leftrightarrow",
        }
        text = "\\underbrace{"
        bottom = False
        for child in root:
            if child.tag == qn("m:groupChrPr"):
                for child2 in child:
                    if child2.tag == qn("m:chr"):
                        char = child2.attrib.get(qn("m:val"))
                        if char in character_map:
                            text = character_map[char]
                for child2 in child:
                    if (
                        child2.tag == qn("m:pos")
                        and child2.attrib.get(qn("m:val")) == "top"
                    ):
                        # If m:pos is set to "top", the symbol is supposed to
                        # be on top and the text is actually supposed to be under
                        bottom = True

        content = ""
        for child in root:
            if child.tag == qn("m:e"):
                content = self.parse(child)
        if text == "\\underbrace{":
            if bottom:
                text = "\\overbrace{" + content + "}"
            else:
                text += content + "}"
        else:
            if not bottom:
                text = "\\overset{" + content + "}" + "{" + text + "}"
            else:
                text = "\\underset{" + content + "}" + "{" + text + "}"
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
            "⟨": "\\left\\langle",
            "⟩": "\\right\\rangle",
            "⌊": "\\left\\lfloor",
            "⌋": "\\right\\rfloor",
            "⌈": "\\left\\lceil",
            "⌉": "\\right\\rceil",
            "|": "\\left|",
            "‖": "\\left\\|",
            "⟦": "[\\![",
            "⟧": "]\\!]",
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
        end_bracket_replacements = {
            "|": "\\right|",
            "‖": "\\right\\|",
            "[": "\\right[",
        }
        start_bracket_replacements = {
            "]": "\\left]",
        }
        if start_bracket:
            if start_bracket in start_bracket_replacements:
                text = start_bracket_replacements[start_bracket] + " " + text
            else:
                text = bracket_map[start_bracket] + " " + text
        if end_bracket:
            if end_bracket in end_bracket_replacements:
                text += " " + end_bracket_replacements[end_bracket]
            else:
                text += " " + bracket_map[end_bracket]
        return text

    def parse_eq_arr(self, root: Element) -> str:
        text = "\\begin{eqnarray*}"
        for child in root:
            if child.tag == qn("m:e"):
                text += self.parse(child) + " \\\\"
        text += "\\end{eqnarray*}"
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

    def parse_func(self, root: Element) -> str:
        function_map = {
            "sin": "\\sin",
            "cos": "\\cos",
            "tan": "\\tan",
            "cot": "\\cot",
            "sec": "\\sec",
            "csc": "\\csc",
            "sinh": "\\sinh",
            "cosh": "\\cosh",
            "tanh": "\\tanh",
            "coth": "\\coth",
            "sech": "\\operatorname{sech}",
            "csch": "\\operatorname{csch}",
            "log": "\\log",
            "ln": "\\ln",
            "min": "\\min",
            "max": "\\max",
            "lim": "\\lim",
        }
        subscript = ""
        superscript = ""
        text = ""
        func_name = "sin"
        for child in root:
            if child.tag == qn("m:fName"):
                for child2 in child:
                    if child2.tag in [qn("m:sSup"), qn("m:sSub"), qn("m:r")]:
                        for child3 in child2:
                            if child3.tag == qn("m:sub"):
                                subscript = self.parse(child3)
                            if child3.tag == qn("m:sup"):
                                superscript = self.parse(child3)
                            if child3.tag == qn("m:t") or child3.tag == qn("m:e"):
                                func_name = self.parse(child3)
                    elif child2.tag == qn("m:limLow"):
                        for child3 in child2:
                            if child3.tag == qn("m:lim"):
                                for child4 in child3:
                                    subscript += self.parse(child4)
                            if child3.tag == qn("m:e"):
                                func_name = self.parse(child3)

            if child.tag == qn("m:e"):
                text += self.parse(child)
        if func_name in ["lim", "max", "min"]:
            return f"\\{func_name}\\limits_{{{subscript}}}^{{{superscript}}}{{{text}}}"
        if func_name not in function_map:
            return f"{{{func_name}}}^{{{superscript}}}_{{{subscript}}}{{{text}}}"
        return function_map[func_name] + f"_{{{subscript}}}^{{{superscript}}}{{{text}}}"

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
        qn("m:box"): parse_box,
        qn("m:d"): parse_d,
        qn("m:e"): parse_e,
        qn("m:groupChr"): parse_group_chr,
        qn("m:f"): parse_f,
        qn("m:sSup"): parse_s_sup,
        qn("m:sSub"): parse_s_sub,
        qn("m:sSubSup"): parse_s_sub_sup,
        qn("m:sPre"): parse_s_pre,
        qn("m:t"): parse_t,
        qn("m:rad"): parse_rad,
        qn("m:nary"): parse_nary,
        qn("m:eqArr"): parse_eq_arr,
        qn("m:func"): parse_func,
    }
