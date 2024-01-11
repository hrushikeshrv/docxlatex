import unittest

from docxlatex import Document


class SimpleTextExtractionTestCase(unittest.TestCase):
    def test_something(self):
        doc = Document('./docx/simple-text.docx')
        text = doc.get_text().strip()
        expected = "Test Document\n\nThis is paragraph 1."
        self.assertEqual(text, expected)


if __name__ == '__main__':
    unittest.main()
