from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar(
    r"""
    program     = if expr+
    expr        = term (operator term)*
    term        = (lpar expr rpar) / word

    if          = "if" ws
    and         = "and"
    or          = "or"
    operator    = ws? (and / or) ws?

    word        = ~"\w+"
    lpar        = "("
    rpar        = ")"

    ws          = ~"\s*"
    """)


class ParExprVisitor(NodeVisitor):

    def __init__(self):
        self.depth = 0
        self.par_expr = []

    def visit_term(self, node, visited_children):
        if self.depth == 0:
            self.par_expr.append(node.text)

    def visit_lpar(self, node, visited_children):
        self.depth += 1

    def visit_rpar(self, node, visited_children):
        self.depth -= 1

    def generic_visit(self, node, visited_children):
        return self.par_expr


tree = grammar.parse("if ((a1 and b) or (a2 and c)) or (c and d) or (e and f)")
print(tree)
visitor = ParExprVisitor()

for expr in visitor.visit(tree):
    print(expr)