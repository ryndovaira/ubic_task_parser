import ast
import json

op_types = {
    ast.Eq: '=',
    ast.Gt: '>',
    ast.GtE: '>=',
    ast.Lt: '<',
    ast.LtE: '<=',
    ast.NotEq: '!='
}


def parse_tree(tree) -> dict:
    dict_tmp = {}
    if isinstance(tree, ast.BoolOp):
        dict_tmp['op'] = 'AND' if isinstance(tree.op, ast.And) else 'OR'
    elif isinstance(tree, ast.Compare):

        dict_tmp['op'] = op_types[type(tree.ops[0])]

        dict_tmp['id'] = tree.left.id
        dict_tmp['literal'] = tree.comparators[0].value

    if hasattr(tree, 'values'):
        dict_tmp['type'] = 'node'
        dict_tmp['left'] = parse_tree(tree.values[0])
        dict_tmp['right'] = parse_tree(tree.values[1])
    elif hasattr(tree, 'value'):
        dict_tmp['left'] = parse_tree(tree.value)  # TODO
    else:
        dict_tmp['type'] = 'leaf'

    print()

    return dict_tmp


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

    fixed_query = query.replace('>=', 'ge')
    fixed_query = fixed_query.replace('<=', 'le')
    fixed_query = fixed_query.replace('!=', 'ne')
    fixed_query = fixed_query.replace('=', '==')
    fixed_query = fixed_query.replace('ge', '>=')
    fixed_query = fixed_query.replace('le', '<=')
    fixed_query = fixed_query.replace('ne', '!=')
    fixed_query = fixed_query.replace('AND', 'and')
    fixed_query = fixed_query.replace('OR', 'or')
    result_tree = ast.parse(fixed_query, mode='exec')
    result = parse_tree(result_tree.body[0].value)

    with open(f"{query}.json", "w") as outfile:     # TODO
        json.dump(result, outfile, indent=4, ensure_ascii=False)
    return result
