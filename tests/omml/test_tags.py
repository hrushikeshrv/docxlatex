import unittest
from docxlatex import Document


class TestTags(unittest.TestCase):
    """
    Test the extraction of OMML tags independently
    with very simple nesting or no nesting of tags.
    """

    def test_r(self):
        text = Document("./docx/tags/r/r.docx").get_text(linear_format=False).strip()
        self.assertEqual(text, "$ a+b+c+d $")

    def test_acc(self):
        text = (
            Document("./docx/tags/acc/dot.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\dot{a} $", text)
        text = (
            Document("./docx/tags/acc/ddot.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\ddot{a} $", text)
        text = (
            Document("./docx/tags/acc/tdot.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\dddot{a} $", text)
        text = (
            Document("./docx/tags/acc/hat.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\hat{a} $", text)
        text = (
            Document("./docx/tags/acc/check.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\check{a} $", text)
        text = (
            Document("./docx/tags/acc/tilde.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\tilde{a} $", text)
        text = (
            Document("./docx/tags/acc/acute.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\acute{a} $", text)
        text = (
            Document("./docx/tags/acc/grave.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\grave{a} $", text)
        text = (
            Document("./docx/tags/acc/breve.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\breve{a} $", text)
        text = (
            Document("./docx/tags/acc/bar.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bar{a} $", text)
        text = (
            Document("./docx/tags/acc/dbar.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\overline{\\overline{a}} $", text)
        text = (
            Document("./docx/tags/acc/overleftarrow.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overleftarrow{a} $", text)
        text = (
            Document("./docx/tags/acc/overrightarrow.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overrightarrow{a} $", text)
        text = (
            Document("./docx/tags/acc/overleftrightarrow.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overset\\leftrightarrow{a} $", text)
        text = (
            Document("./docx/tags/acc/leftharpoon.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overset\\leftharpoonup{a} $", text)
        text = (
            Document("./docx/tags/acc/rightharpoon.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overset\\rightharpoonup{a} $", text)
        text = (
            Document("./docx/tags/acc/tilde-bar.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bar{\\tilde{a}} $", text)

    def test_border_box(self):
        text = (
            Document("./docx/tags/borderBox/borderBox.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\boxed{a} $", text)
        text = (
            Document("./docx/tags/borderBox/boxedFormula.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\boxed{boxed formula} $", text)

    def test_bar(self):
        text = (
            Document("./docx/tags/bar/overline.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overline{asdf} $", text)
        # Section 22.1.2.8 of the spec says that the pos child of the barPr element
        # must have value either top or bot, but the test document does not have a pos child.
        # Therefore, the default value is top and docxlatex will return an overline instead of
        # an underline.
        text = (
            Document("./docx/tags/bar/underline.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overline{asdf} $", text)
        text = (
            Document("./docx/tags/bar/overline-tilde.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overline{\\tilde{a}sdf} $", text)

    def test_group_chr(self):
        text = (
            Document("./docx/tags/groupChr/overbrace.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\overbrace{asdf} $", text)
        text = (
            Document("./docx/tags/groupChr/underbrace.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\underbrace{asdf} $", text)

    def test_f(self):
        text = Document("./docx/tags/f/f.docx").get_text(linear_format=False).strip()
        self.assertEqual("$ \\frac{abc}{def} $", text)
        text = Document("./docx/tags/f/dydx.docx").get_text(linear_format=False).strip()
        self.assertEqual("$ \\frac{dy}{dx} $", text)

    def test_s_sup(self):
        text = (
            Document("./docx/tags/sSup/exponent.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {a}^{b} $", text)
        text = (
            Document("./docx/tags/sSup/abcdef.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {abc}^{def} $", text)

    def test_s_sub(self):
        text = (
            Document("./docx/tags/sSub/subscript.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {a}_{b} $", text)
        text = (
            Document("./docx/tags/sSub/abcdef.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {abc}_{def} $", text)

    def test_s_sub_sup(self):
        text = (
            Document("./docx/tags/sSubSup/sub_sup.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {a}_{b}^{c} $", text)
        text = (
            Document("./docx/tags/sSubSup/abcdefghi.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {abc}_{def}^{ghi} $", text)

    def test_s_pre(self):
        text = (
            Document("./docx/tags/sPre/pre_sub_sup.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ {}^{b}_{a}{c} $", text)

    def test_rad(self):
        text = (
            Document("./docx/tags/rad/sqrt.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sqrt{a} $", text)
        text = (
            Document("./docx/tags/rad/cube_root.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\sqrt[3]{a} $", text)
        text = (
            Document("./docx/tags/rad/nth_root.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\sqrt[n]{a} $", text)

    def test_nary(self):
        text = (
            Document("./docx/tags/nary/integral.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\int{x dx} $", text)
        text = (
            Document("./docx/tags/nary/integral2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\int_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/integral3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\int_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/iint.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\iint{xy dxdy} $", text)
        text = (
            Document("./docx/tags/nary/iint2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\iint_{0}^{1}{xy dxdy} $", text)
        text = (
            Document("./docx/tags/nary/iint3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\iint_{0}^{1}{xy dxdy} $", text)
        text = (
            Document("./docx/tags/nary/iiint.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\iiint{x dx} $", text)
        text = (
            Document("./docx/tags/nary/iiint2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\iiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/iiint3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\iiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oint.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\oint{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oint2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oint3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiint.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiint{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiint2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiint3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiiint.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiiint{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiiint2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/oiiint3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\oiiint_{0}^{1}{x dx} $", text)
        text = (
            Document("./docx/tags/nary/sum.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sum{i} $", text)
        text = (
            Document("./docx/tags/nary/sum2.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sum_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/sum3.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sum_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/sum4.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sum_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/sum5.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\sum_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/prod.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\prod{i} $", text)
        text = (
            Document("./docx/tags/nary/prod2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\prod_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/prod3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\prod_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/prod4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\prod_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/prod5.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\prod_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/coprod.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\coprod{i} $", text)
        text = (
            Document("./docx/tags/nary/coprod2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\coprod_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/coprod3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\coprod_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/coprod4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\coprod_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/coprod5.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\coprod_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/cup.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcup{i} $", text)
        text = (
            Document("./docx/tags/nary/cup2.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcup_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/cup3.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcup_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/cup4.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcup_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/cup5.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcup_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/cap.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcap{i} $", text)
        text = (
            Document("./docx/tags/nary/cap2.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcap_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/cap3.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcap_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/cap4.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcap_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/cap5.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\bigcap_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigvee.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigvee{i} $", text)
        text = (
            Document("./docx/tags/nary/bigvee2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigvee_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigvee3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigvee_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigvee4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigvee_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigvee5.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigvee_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigwedge.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigwedge{i} $", text)
        text = (
            Document("./docx/tags/nary/bigwedge2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigwedge_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigwedge3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigwedge_{0}^{1}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigwedge4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigwedge_{0}{i} $", text)
        text = (
            Document("./docx/tags/nary/bigwedge5.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\bigwedge_{0}{i} $", text)

    def test_d(self):
        text = (
            Document("./docx/tags/d/parenthesis.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left( asdf \\right) $", text)
        text = (
            Document("./docx/tags/d/square_brackets.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left[ a b c d \\right] $", text)
        text = (
            Document("./docx/tags/d/square_brackets_2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left[ a \\right[ $", text)
        text = (
            Document("./docx/tags/d/square_brackets_3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left] a \\right] $", text)
        text = (
            Document("./docx/tags/d/square_brackets_4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left] a \\right[ $", text)
        text = (
            Document("./docx/tags/d/curly_brackets.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left{ a b c d \\right} $", text)
        text = (
            Document("./docx/tags/d/angle_brackets.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left\\langle a b c d \\right\\rangle $", text)
        text = (
            Document("./docx/tags/d/floor.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\left\\lfloor a b c d \\right\\rfloor $", text)
        text = Document("./docx/tags/d/ceil.docx").get_text(linear_format=False).strip()
        self.assertEqual("$ \\left\\lceil a b c d \\right\\rceil $", text)
        text = Document("./docx/tags/d/abs.docx").get_text(linear_format=False).strip()
        self.assertEqual("$ \\left| a b c d \\right| $", text)
        text = Document("./docx/tags/d/norm.docx").get_text(linear_format=False).strip()
        self.assertEqual("$ \\left\\| a b c d \\right\\| $", text)
        text = (
            Document("./docx/tags/d/double_brackets.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ [\\![ a ]\\!] $", text)
        text = (
            Document("./docx/tags/d/parenthesis_2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left( a|b \\right) $", text)
        text = (
            Document("./docx/tags/d/parenthesis_3.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ \\left( a $", text)
        text = (
            Document("./docx/tags/d/parenthesis_4.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual("$ a \\right) $", text)

    def test_eq_array(self):
        text = (
            Document("./docx/tags/eqArr/stack.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ \\begin{cases} a \\\\b \\\\ \\end{cases} $", text
        )
        text = (
            Document("./docx/tags/eqArr/stack2.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ \\begin{cases} a \\\\b \\\\c \\\\ \\end{cases} $", text
        )

        text = (
            Document("./docx/tags/eqArr/issue_9.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ f\\left( n \\right)=\\begin{cases} \\left\\langle 0,0 \\right\\rangle,&{χ}_{TH}(n)=1 \\\\\\left\\langle 0,m \\right\\rangle, &otherwise \\\\ \\end{cases} $",
            text
        )

    def test_func(self):
        text = (
            Document("./docx/tags/func/trig.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual(
            "$ \\sin_{}^{}{x} \\cos_{}^{}{x} \\tan_{}^{}{x} \\csc_{}^{}{x} \\sec_{}^{}{x} \\cot_{}^{}{x} $",
            text,
        )
        text = (
            Document("./docx/tags/func/inverse_trig.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ \\sin_{}^{-1}{x} \\cos_{}^{-1}{x} \\tan_{}^{-1}{x} \\csc_{}^{-1}{x} \\sec_{}^{-1}{x} \\cot_{}^{-1}{x} $",
            text,
        )
        text = (
            Document("./docx/tags/func/hyperbolic.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ \\sinh_{}^{}{x} \\cosh_{}^{}{x} \\tanh_{}^{}{x} \\operatorname{csch}_{}^{}{x} \\operatorname{sech}_{}^{}{x} \\coth_{}^{}{x} $",
            text,
        )
        text = (
            Document("./docx/tags/func/inverse_hyperbolic.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            "$ \\sinh_{}^{-1}{x} \\cosh_{}^{-1}{x} \\tanh_{}^{-1}{x} \\operatorname{csch}_{}^{-1}{x} \\operatorname{sech}_{}^{-1}{x} \\coth_{}^{-1}{x} $",
            text,
        )
        text = (
            Document("./docx/tags/func/log.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\log_{a}^{}{b} $", text)
        text = (
            Document("./docx/tags/func/log2.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\log_{}^{}{a} $", text)
        text = (
            Document("./docx/tags/func/log3.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\ln_{}^{}{a} $", text)
        text = (
            Document("./docx/tags/func/lim.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\lim\\limits_{a}^{}{b} $", text)
        text = (
            Document("./docx/tags/func/max.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\max\\limits_{a}^{}{b} $", text)
        text = (
            Document("./docx/tags/func/min.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual("$ \\min\\limits_{a}^{}{b} $", text)


if __name__ == "__main__":
    unittest.main()
