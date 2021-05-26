import zipfile
from xml.etree import ElementTree


def qualified_name(tag):
    """
    :param tag:str - A namespace-prefixed tag name
    :return qn:str - A Clark-notation qualified name tag for lxml.
    
    A utility function to turn a namespace
    prefixed tag name into a Clark-notation qualified tag name for lxml. For
    example, qualified_name('p:cSld') returns '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cSld'
    Source: https://github.com/python-openxml/python-docx/
    """
    ns_map = {
        'w': 'http://schemas.opensmlformats.org/wordprocessingml/2006/main'
    }
    prefix, tag_root = tag.split(':')
    uri = ns_map[prefix]
    return '{{{}}}{}'.format(uri, tag_root)


def xml_to_text(xml):
    """
    :param xml:str - XML string to be parsed into an xml.etree.Element object.
    :return text:str - The text contained in the tag
    
    Recursively iterate over the ElementTree of the word document and extract text content from supported tags.
    """
    text = ''
    root = ElementTree.fromstring(xml)
    for child in root.iter():
        if child.tag == qualified_name('w:t') or 'math' in child.tag.lower():
            text += child.text if child.text is not None else ''
        elif child.tag == qualified_name('w:tab'):
            text += '\t'
        elif child.tag == qualified_name('w:br') or child.tag == qualified_name('w:cr'):
            text += '\n'
        elif child.tag == qualified_name('w:p'):
            text += '\n\n'
    
    return text


def get_text(doc_path):
    """
    :param doc_path:str - The full path to the word document to be read
    :return text:str - The extracted text from the document (this is where you get the latex)
    
    The whole point of this library. Takes in the path to the .docx document and
    extracts text from it. For now, requires all the equations in the document to be converted to linear.
    
    TODOS-
        1. Clean up some equations that convert into linear but do not give valid LaTeX.
    """
    zip_f = zipfile.ZipFile(doc_path)
    text = ''
    for f in zip_f.namelist():
        if f.startswith('word/document') or f.startswith('word/header') or f.startswith('word/footer'):
            text += xml_to_text(zip_f.read(f))
            
    return text
