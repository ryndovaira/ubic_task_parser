from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar

grammar = Grammar(
    r"""
    all_query = (lb? query rb?) / (lb? all_query rb?)
    query = lb? subquery (space? lop space? subquery)* rb?
    subquery = (lb? space? id space? op space? literal space? rb?) / (lb? query rb?)
    lb        = "("
    rb        = ")" 
    lop = "AND" / "OR"
    id = ~"(\w+)"
    op = "=" / "!=" / ">=" / "<=" / ">" / "<"
    literal = number / string
    string = ~"(\"\w+\")"
    number = ~"-?\d*\.\d+" / ~"-?\d+"
    space = ~"\s+"
    """)


class ParExprVisitor(NodeVisitor):

    def __init__(self):
        self.depth = 0
        self.par_expr = []
        self.tree = {}

    def visit_all_query(self, node, visited_children):
        # if self.depth == 0:
        #     self.par_expr.append(node.text)
        return node.text

    def visit_query(self, node, visited_children):
        # self.depth += 1
        return node.text

    def visit_subquery(self, node, visited_children):
        # self.depth -= 1
        return node.text

    def visit_id(self, node, visited_children):
        return node.text

    def visit_literal(self, node, visited_children):
        return node.text

    def visit_lop(self, node, visited_children):
        return node.text

    def visit_op(self, node, visited_children):
        return node.text

    def generic_visit(self, node, visited_children):
        # return self.par_expr
        return node.text


def parse(query: str) -> dict:
    """
    Парсит логический запрос в дерево операций
    @param query: логический запрос вида 'Пол="М" AND (Возраст>25 OR Стаж>5)'.
    Поддерживаемые операции сравнения: = != > < >= <=
    Поддерживаемые логические операции: AND OR, приоритет одинаковый, группировка скобками
    Поддерживаемые типы литералов: int float str (двойные кавычки внутри строки не допускаются)
    @return: словарь, содержащий дерево операций (см. ассерты)
    Поддерживаемые типы узлов (type):
    leaf - узел, представляющий операцию сравнения
    node - узел, представляющий логическую операцию, имеет два подузла - left, right
    """

    # Необходимо написать функцию, пользуясь любыми библиотеками или без них.
    # Также необходимо написать 3-5 ассертов на разные граничные случаи:
    # разную расстановку скобок, синтаксические ошибки в выражении и т.п.
    # При использовании сторонних библиотек парсинга необходимо написать 5-10 ассертов,
    # т.е. проверить как можно больше граничных случаев.

    result = grammar.parse(query)
    print(result)

    visitor = ParExprVisitor()
    return visitor.visit(result)
    # for expr in visitor.visit(result):
    #     print(expr)
