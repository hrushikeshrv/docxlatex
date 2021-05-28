"""
    Utility functions to extract text from different mathematical equations and
    convert them into LaTeX
"""


ns_map = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
}


def tag_to_latex(tag):
    text = ''
    exp = ''
    for child in tag.iter():
        if child.tag == qn('m:chr'):
            exp = child.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val')
    text += supported_exps[exp](tag)
    return text


def sigma(tag):
    """
    Constructs LaTeX of the form \\sum_{}^{}{}
    :return latex:str - A sigma expression
    """
    latex = '\\sum_{{{}}}^{{{}}}{{{}}}'
    blocks = ['', '', '']
    curr_block = 0
    for child in tag.iter():
        child.set('docxlatex_skip_iteration', True)
        if child.tag == qn('m:sub'):
            curr_block = 0
        elif child.tag == qn('m:sup'):
            curr_block = 1
        elif child.tag == qn('m:e'):
            curr_block = 2
        blocks[curr_block] += child.text if child.text is not None else ''
    
    return latex.format(blocks[0], blocks[1], blocks[2])


def qn(tag):
    """
    A utility function to turn a namespace
    prefixed tag name into a Clark-notation qualified tag name for lxml. For
    example, qualified_name('p:cSld') returns '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cSld'
    Source: https://github.com/python-openxml/python-docx/

    :param tag:str - A namespace-prefixed tag name
    :return qn:str - A Clark-notation qualified name tag for lxml.
    """
    prefix, tag_root = tag.split(':')
    uri = ns_map[prefix]
    return '{{{}}}{}'.format(uri, tag_root)


supported_exps = {
    '∑': sigma,
}
