"""
    Utility functions to extract text from the supported mathematical equations from xml tags and
    convert them into LaTeX
"""
from cleaners import clean_exp

ns_map = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}


def tag_to_latex(tag):
    # exp = ''
    # for child in tag.iter():
    #     if child.tag == qn('m:chr'):
    #         exp = child.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val')
    #     elif child.tag == qn('m:f'):
    #         exp = 'frac'
    #         break
    # if exp == '':
    #     return linear_expression(tag)
    # text = ''
    # try:
    #     text += supported_exps[exp](tag)
    # except KeyError:
    #     text += linear_expression(tag)
    return linear_expression(tag)


def linear_expression(tag):
    """
    Just returns the text contained in the given tag while setting defusedxml_skip_iteration flags
    for all its children.
    :param tag:defusedxml.Element - An xml element which contains a math equation in linear form
    :return text:str - The equation in valid LaTeX syntax
    """
    text = ""
    for child in tag.iter():
        child.set("docxlatex_skip_iteration", True)
        text += child.text if child.text is not None else ""
    text = clean_exp(text)
    return text


def qn(tag):
    """
    A utility function to turn a namespace
    prefixed tag name into a Clark-notation qualified tag name for lxml. For
    example, qn('m:oMath') returns '{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath'

    :param tag:str - A namespace-prefixed tag name
    :return qn:str - A Clark-notation qualified name tag for lxml.
    """
    prefix, tag_root = tag.split(":")
    uri = ns_map[prefix]
    return "{{{}}}{}".format(uri, tag_root)
