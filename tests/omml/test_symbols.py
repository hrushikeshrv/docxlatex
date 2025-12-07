from docxlatex import Document
import unittest


class TestSymbols(unittest.TestCase):
    def test_operators(self):
        """Test extraction of operators and operator structures found in the Equation > Operator menu."""
        text = Document("./docx/operators.docx").get_text(linear_format=False).strip()
        self.assertEqual(
            text,
            "$ ∶= == += -=\\stackrel{\\tiny def}{=} \\stackrel{\\tiny m}{=} \\triangleq $",
        )
        text = (
            Document("./docx/operator_structures.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ \\underset{a}{\\leftarrow} \\underset{a}{\\rightarrow} \\overset{a}{\\leftarrow} \\overset{a}{\\rightarrow} \\underset{a}{\\Leftarrow} \\underset{a}{\\Rightarrow} \\overset{a}{\\Leftarrow} \\overset{a}{\\Rightarrow} \\underset{a}{\\leftrightarrow} \\overset{a}{\\leftrightarrow} \\underset{a}{\\Leftrightarrow} \\overset{a}{\\Leftrightarrow} $",
        )

    def test_basic_math_symbols(self):
        text = (
            Document("./docx/basic_math_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ ±\\infty =≠~×÷!∝\\lt ≪\\gt ≫\\leq \\geq ∓≅≈≡∀∁∂√∛∜∪∩∅%°℉℃∆∇∃∄∈∋←↑→↓↔∴+-¬αβγδεϵθϑμπρστφω*∙⋮⋯⋰⋱ℵℶ∎ $",
        )

    def test_greek_letters(self):
        text = (
            Document("./docx/greek_letters.docx").get_text(linear_format=False).strip()
        )
        self.assertEqual(
            text,
            "$ αβγδεϵζηθϑικλμνξοπϖρϱσςτυφϕχψω $\n\n$ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ $",
        )

    def test_letter_like_symbols(self):
        # TODO: Add support for different scripts of all letter-like symbols
        text = (
            Document("./docx/letter_like_symbols.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ ∀∁C∂ðℇϜℲgHHhℏ℩ıIjϰLlN℘QRRRZ℧ÅB℮E∃∄FMoℵℶℷℸ $",
        )

    def test_common_binary_operators(self):
        text = (
            Document("./docx/common_binary_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ +-÷×±∓∝∕*∘∙⋅∩∪⊎⊓⊔∧∨ $",
        )

    def test_common_relational_operators(self):
        text = (
            Document("./docx/common_relational_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ =≠\\lt \\gt \\leq \\geq ≮≰≯≱≡∼≃≈≅≢≄≉≇∝≪≫∈∋∉⊂⊃⊆⊇≺≻≼≽⊏⊐⊑⊒∥⊥⊢⊣⋈≍ $",
        )

    def test_basic_nary_operators(self):
        text = (
            Document("./docx/basic_nary_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ ∑∫∬∭∮∯∰∱∲∳∏∐⋂⋃⋀⋁⨀⨂⨁⨄⨃ $",
        )

    def test_advanced_binary_operators(self):
        text = (
            Document("./docx/advanced_binary_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ ∔∸∖⋒⋓⊟⊠⊡⊞⋇⋉⋊⋋⋌⋏⋎⊝⊺⊕⊖⊗⊘⊙⊛⊚†‡⋆⋄≀△⋀⋁⨀⨂⨁⨅⨆⨄⨃ $",
        )

    def test_advanced_relational_operators(self):
        text = (
            Document("./docx/advanced_relational_operators.docx")
            .get_text(linear_format=False)
            .strip()
        )
        self.assertEqual(
            text,
            "$ ∴∵⋘⋙≦≧≲≳⋖⋗≶⋚≷⋛≑≒≓∽≊⋍≼≽⋞⋟≾≿⋜⋝⊆⊇⊲⊳⊴⊵⊨⋐⋑⊏⊐⊩⊪≖≗≜≏≎∝≬⋔≐⋈ $",
        )


if __name__ == "__main__":
    unittest.main()
