import unittest
from docxlatex import Document


class TestTags(unittest.TestCase):
    """
    Test the extraction of OMML tags independently
    with very simple nesting or no nesting of tags.
    """

    def test_r(self):
        text = Document('./docx/tags/r/r.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ a+b+c+d $')

    def test_acc(self):
        text = Document('./docx/tags/acc/dot.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\dot{a} $', text)
        text = Document('./docx/tags/acc/ddot.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\ddot{a} $', text)
        text = Document('./docx/tags/acc/tdot.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\dddot{a} $', text)
        text = Document('./docx/tags/acc/hat.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\hat{a} $', text)
        text = Document('./docx/tags/acc/check.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\check{a} $', text)
        text = Document('./docx/tags/acc/tilde.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\tilde{a} $', text)
        text = Document('./docx/tags/acc/acute.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\acute{a} $', text)
        text = Document('./docx/tags/acc/grave.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\grave{a} $', text)
        text = Document('./docx/tags/acc/breve.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\breve{a} $', text)
        text = Document('./docx/tags/acc/bar.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\bar{a} $', text)
        text = Document('./docx/tags/acc/dbar.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overline{\\overline{a}} $', text)
        text = Document('./docx/tags/acc/overleftarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overleftarrow{a} $', text)
        text = Document('./docx/tags/acc/overrightarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overrightarrow{a} $', text)
        text = Document('./docx/tags/acc/overleftrightarrow.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overset\\leftrightarrow{a} $', text)
        text = Document('./docx/tags/acc/leftharpoon.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overset\\leftharpoonup{a} $', text)
        text = Document('./docx/tags/acc/rightharpoon.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overset\\rightharpoonup{a} $', text)
        text = Document('./docx/tags/acc/tilde-bar.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\bar{\\tilde{a}} $', text)

    def test_border_box(self):
        text = Document('./docx/tags/borderBox/borderBox.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\boxed{a} $', text)
        text = Document('./docx/tags/borderBox/boxedFormula.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\boxed{boxed formula} $', text)

    def test_bar(self):
        text = Document('./docx/tags/bar/overline.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overline{asdf} $', text)
        # Section 22.1.2.8 of the spec says that the pos child of the barPr element
        # must have value either top or bot, but the document does not have a pos child.
        # Therefore, the default value is top and docxlatex will return an overline instead of
        # an underline.
        text = Document('./docx/tags/bar/underline.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overline{asdf} $', text)
        text = Document('./docx/tags/bar/overline-tilde.docx').get_text(linear_format=False).strip()
        self.assertEqual('$ \\overline{\\tilde{a}sdf} $', text)


if __name__ == '__main__':
    unittest.main()
