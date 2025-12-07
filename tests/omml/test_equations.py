import unittest
from docxlatex import Document


class TestEquations(unittest.TestCase):
    def test_equations(self):
        text = Document("./docx/binomial-theorem.docx").get_text().strip()
        self.assertEqual(
            text,
            "$ {\\left( x+a \\right)}^{n}=\\sum_{k=0}^{n}{\\left( \\genfrac{}{}{0pt}{}{n}{k} \\right){x}^{k}{a}^{n-k}} $",
        )

        text = Document("./docx/fourier_series.docx").get_text().strip()
        self.assertEqual(
            text,
            "$ f\\left( x \\right)={a}_{0}+\\sum_{n=1}^{\\infty }{\\left( {a}_{n}\\cos_{}^{}{\\frac{nπx}{L}}+{b}_{n}\\sin_{}^{}{\\frac{nπx}{L}} \\right)} $",
        )

        text = Document("./docx/taylor_expansion.docx").get_text().strip()
        self.assertEqual(
            text,
            "$ {e}^{x}=1+\\frac{x}{1!}+\\frac{{x}^{2}}{2!}+\\frac{{x}^{3}}{3!}+…, -\\infty \\lt x\\lt \\infty  $",
        )


if __name__ == "__main__":
    unittest.main()
