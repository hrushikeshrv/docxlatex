import os
import unittest
from docxlatex import Document


class TestTags(unittest.TestCase):
    """
    Test the extraction of OMML tags.
    """

    def test_r(self):
        text = Document('../docx/tags/r.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ a+b+c+d $')

    def test_acc(self):
        text = Document('../docx/tags/acc/hat.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\hat{a} $')
        text = Document('../docx/tags/acc/dot.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\dot{a} $')


if __name__ == '__main__':
    unittest.main()
