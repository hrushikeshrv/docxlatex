# docxlatex
A python library for extracting text from .docx files with LaTeX support

Influenced by [python-docx](https://github.com/python-openxml/python-docx) and [python-docx2txt](https://github.com/ankushshah89/python-docx2txt).
This project aims to expand the above libraries' functionality by allowing you to extract the equations in a .docx file and converts them to valid LaTeX, 
primarily for use with MathJax.

docxlatex DOES NOT convert the entire .docx file to a LaTeX source file.

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
and flags to extract header and footer text.

```python
doc.get_header_text = True # False by default
doc.get_footer_text = True # False by default
doc.inline_delimiter = "%" # "$" by default
doc.block_delimiter = "%%" # "$$" by default
```

# Limitation
docxlatex currently requires all the mathematical equations in the .docx document to be converted into linear format to extract successfully. I am adding support for 
equations in the professional format right now. Soon you will be able to use it without having to use this workaround, but for now, open the .docx file in Word, click on any equation, click on the right context menu > All - linear.

# TODOs
- [ ] Extract all images present in the file and return them as file-like objects
- [ ] Add support for equations in professional formatting
- [ ] Clean up equations in linear format that do not directly convert to valid LaTeX
