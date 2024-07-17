import unittest

from docxlatex import Document


class SimpleTextExtractionTestCase(unittest.TestCase):
    def test_simple_text_extraction(self):
        doc = Document('./docx/simple-text.docx')
        text = doc.get_text().strip()
        expected = "Test Document\n\nThis is paragraph 1."
        self.assertEqual(text, expected)

    def test_simple_equation_extraction_linear_format(self):
        doc = Document('./docx/simple-equation-linear-format.docx')
        text = doc.get_text().strip()
        expected = '$ a^2+b^2=c^2 $'
        self.assertEqual(text, expected)


if __name__ == '__main__':
    unittest.main()
