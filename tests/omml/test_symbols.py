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
            "$ ±∞=≠~×÷!∝<≪>≫≤≥∓≅≈≡∀∁∂√∛∜∪∩∅%°℉℃∆∇∃∄∈∋←↑→↓↔∴+-¬αβγδεϵθϑμπρστφω*∙⋮⋯⋰⋱ℵℶ∎ $",
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


if __name__ == "__main__":
    unittest.main()
