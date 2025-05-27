# Specification
This collection of files lists the OMML tags (i.e. the types of operators and functions) that docxlatex will support, will not support, and will ignore. There are a total of 124 math tags defined in the [formal ECMA specification](https://ecma-international.org/publications-and-standards/standards/ecma-376/) for OMML. You can download the formal specification from [the ECMA website](https://ecma-international.org/wp-content/uploads/ECMA-376-1_5th_edition_december_2016.zip).

Chapter 22 in the `Ecma Office Open XML Part 1 - Fundamentals And Markup Language Reference` document lists all OMML tags, which you can refer to determine whether the tag you are interested in is supported by docxlatex.

- [Supported tags](./supported-tags.md) will be extracted and converted into LaTeX correctly 
- [Unsupported tags](./unsupported-tags.md) will be extracted but may not convert to LaTeX correctly, or their properties may not be applied correctly during extraction
- [Ignored tags](./ignored-tags.md) will not be extracted and their properties will not be considered during extraction.