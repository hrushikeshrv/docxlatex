import os
import unittest
from docxlatex import Document


class TestTags(unittest.TestCase):
    """
    Test the extraction of OMML tags.
    """

    def test_r(self):
        text = Document('../docx/tags/r.docx').get_text(linear_format=False).strip()
        self.assertEqual(text, '$ a+b+c+d $')  # add assertion here


if __name__ == '__main__':
    unittest.main()
