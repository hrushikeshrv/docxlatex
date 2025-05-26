from docxlatex import Document
import unittest


class TestSymbols(unittest.TestCase):
    def test_operators(self):
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


if __name__ == "__main__":
    unittest.main()
