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
        text = Document('../docx/tags/acc/dot.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\dot{a} $')
        text = Document('../docx/tags/acc/ddot.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\ddot{a} $')
        text = Document('../docx/tags/acc/tdot.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\dddot{a} $')
        text = Document('../docx/tags/acc/hat.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\hat{a} $')
        text = Document('../docx/tags/acc/check.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\check{a} $')
        text = Document('../docx/tags/acc/tilde.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\tilde{a} $')
        text = Document('../docx/tags/acc/acute.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\acute{a} $')
        text = Document('../docx/tags/acc/grave.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\grave{a} $')
        text = Document('../docx/tags/acc/breve.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\breve{a} $')
        text = Document('../docx/tags/acc/bar.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\bar{a} $')
        text = Document('../docx/tags/acc/dbar.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overline{\\overline{a}} $')
        text = Document('../docx/tags/acc/overleftarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overleftarrow{a} $')
        text = Document('../docx/tags/acc/overrightarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overrightarrow{a} $')
        text = Document('../docx/tags/acc/overleftrightarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overset\\leftrightarrow{a} $')
        text = Document('../docx/tags/acc/leftharpoon.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overset\\leftharpoonup{a} $')
        text = Document('../docx/tags/acc/rightharpoon.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ \\overset\\rightharpoonup{a} $')


if __name__ == '__main__':
    unittest.main()
