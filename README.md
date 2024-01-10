# docxlatex
A python library for extracting text and images from .docx files with LaTeX support

Influenced by [python-docx](https://github.com/python-openxml/python-docx) and [python-docx2txt](https://github.com/ankushshah89/python-docx2txt).
This project aims to expand the above libraries' functionality by allowing you to extract the equations in a .docx file and converts them to valid LaTeX, 
primarily for use with MathJax.

docxlatex DOES NOT convert the entire .docx file to a LaTeX source file.

docxlatex is still in beta and does not work perfectly on all equations. However, 
it does work with reasonable accuracy on standard symbols and equations, and works reliably when the equations in the 
document have been converted to linear format.

# Installation
Install using pip  
`pip install docxlatex`

# Usage

Import the `Document` class from `docxlatex`

```python
from docxlatex import Document
```

Create a `Document` object, giving it the path to the .docx file, and call the `get_text()` method
```python
doc = Document("path/to/document")
text = doc.get_text()
```

You can also set some settings on the `Document` object to customize behaviour, like setting the delimiters that will go before and after an equation, 
and flags to extract header and footer text. Read the documentation at [hrushikeshrv.github.io/docxlatex](https://hrushikeshrv.github.io/docxlatex) for all options.

```python
doc.inline_delimiter = "%" # "$" by default
doc.block_delimiter = "%%" # "$$" by default
```

# Limitation
docxlatex currently requires all the mathematical equations in the .docx document to be converted into linear format to extract successfully. Make sure all the equations in the .docx file are converted into linear form.  

To convert all your equations into linear format, click on any equation, go to the Equation tab, make sure LaTeX is selected, and click on Convert &#8594; All - Linear

Please report any bugs on this project's GitHub page [docxlatex/issues](https://github.com/hrushikeshrv/docxlatex/issues)

