"""

"""
import re

clean_exps = {
    r'\\degf': '&deg;F',
    r'\\degc': '&deg;C',
    r'(\\cbrt)(\w+)': r'\\sqrt[3]{\2}',
    r'(\\qdrt)(\w+)': r'\\sqrt[4]{\2}',
    r'\\sfrac': r'\\frac',
    r'(\\o[i]+nt)(\w+)': r'\1{\2}',
}


def clean_exp(exp):
    """
    Takes in a linear expression and converts known invalid LaTeX equations to valid LaTeX
    :param exp:str - An equation in invalid syntax
    :return :str - A valid equation
    """
    for e in clean_exps:
        exp = re.sub(e, clean_exps[e], exp)
    return exp
