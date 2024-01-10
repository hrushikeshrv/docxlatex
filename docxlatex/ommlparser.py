class Equation:
    """
    Wrapper class representing the equation being extracted. Responsible for
    parsing OMML and building an Equation object
    """
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)
    
    def to_latex(self):
        latex = ''
        for c in self.components:
            latex += c.to_latex() + ' '
        return latex.strip()


class Block:
    """
    Represents a block for a component in the equation
    """
    def __init__(self, parent):
        self.children = []
        self.parent = parent
    
    def add_child(self, component):
        self.children.append(component)
    
    def to_latex(self):
        if len(self.children) == 0:
            return ''
        latex = ''
        for c in self.children:
            if isinstance(c, str):
                latex += c
            else:
                latex += c.to_latex()
        return latex.strip()


class Component:
    """
    Represents a component. Abstract base class to inherit from
    """
    def __init__(self, blocks=None, parent=None):
        if blocks is None:
            blocks = []
        self.blocks = blocks
        self.parent = parent
    
    def to_latex(self):
        raise NotImplementedError('This method is to be overridden in all child classes inheriting from Component')
