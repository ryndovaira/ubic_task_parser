import ast
from ast2json import ast2json

class AnalysisNodeVisitor(ast.NodeVisitor):
    def visit_BinOp(self, node):
        print('Node type: BinOp and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Expr(self, node):
        print('Node type: Expr and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Num(self, node):
        print('Node type: Num and fields: ', node._fields)

    def visit_Name(self, node):
        print('Node type: Name and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Str(self, node):
        print('Node type: Str and fields: ', node._fields)



import pprint
import re

type_lookup = {
    ast.Module: 'Module',
    ast.FunctionDef: 'Function',
    ast.ClassDef: 'Class'
}
pattern = re.compile('[\W_]+')
stopwords = [
    'the','of','and','to','in','be','will','for','on','is', \
    'with', 'by', 'as', 'this', 'are', 'from', 'that', 'or', \
    'at', 'been', 'an', 'was', 'were', 'have', 'has', 'it', ''
]

def parse_tree(node):
    """
    Uses the stack to navigate our parse tree and discover Module, Classes,
    and Functions doc strings and all other comments.
    """

    tree = dict(
        type=type_lookup[type(node)],
        name=node.name if 'name' in node.__dict__ else __file__.split('.')[0],
        doc=ast.get_docstring(node),
        children=[]
    )

    for child in node.body:

        if type(child) not in [ast.Module, ast.FunctionDef, ast.ClassDef]:
            continue

        tree['children'].append(parse_tree(child))

    return tree


def tokenize(text):
    """
    Takes a string and tokenizes it into terms
    """

    output = []
    if not text:
        return output

    for term in text.lower().split(' '):

        term = pattern.sub('', term)
        if term in stopwords:
            continue

        output.append(term)

    return output


def get_terms(node):
    terms = tokenize(node['doc'])
    for child in node['children']:
        child_terms = get_terms(child)
        unique_terms = [term for term in child_terms if term not in terms]
        terms.extend(unique_terms)

    return terms

pt = ast.parse("a==5 and b==88", mode='exec')
print(ast2json(pt))
# tree = parse_tree(pt)
# terms = get_terms(tree)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(tree)
# pp.pprint(terms)
# v = AnalysisNodeVisitor()
# v.visit(pt)
