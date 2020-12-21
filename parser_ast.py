import ast

lop_types = {
    ast.And: 'AND',
    ast.Or: 'OR'
}

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
        try:
            dict_tmp['op'] = lop_types[type(tree.op)]
        except AttributeError:
            raise ValueError('Query contains wrong operator(s)')

    elif isinstance(tree, ast.Compare):
        dict_tmp['op'] = op_types[type(tree.ops[0])]

        dict_tmp['id'] = tree.left.id
        if len(tree.comparators) != 1:
            raise ValueError('Query contains wrong operator(s)')

        if isinstance(tree.comparators[0], ast.UnaryOp):
            if isinstance(tree.comparators[0].op, ast.USub):
                dict_tmp['literal'] = -tree.comparators[0].operand.value
            elif isinstance(tree.comparators[0].op, ast.UAdd):
                dict_tmp['literal'] = +tree.comparators[0].operand.value
            else:
                raise ValueError('Query contains wrong operator(s)')

        elif isinstance(tree.comparators[0], ast.Constant):
            dict_tmp['literal'] = tree.comparators[0].value

        else:
            raise ValueError('Query contains wrong operator(s)')

    else:
        raise ValueError('Query contains wrong operator(s)')

    if hasattr(tree, 'values'):
        dict_tmp['type'] = 'node'
        dict_tmp['left'] = parse_tree(tree.values[0])
        dict_tmp['right'] = parse_tree(tree.values[1])

    else:
        dict_tmp['type'] = 'leaf'

    return dict_tmp


def fix_query(query: str) -> str:
    fixed_query = query.replace('>=', 'ge').replace('<=', 'le').replace('!=', 'ne')

    fixed_query = fixed_query.replace('=', '==')

    fixed_query = fixed_query.replace('ge', '>=').replace('le', '<=').replace('ne', '!=')

    fixed_query = fixed_query.replace('AND', 'and').replace('OR', 'or')
    return fixed_query


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

    if len(query) == 0:
        return {}

    fixed_query = fix_query(query)
    result_tree = ast.parse(fixed_query, mode='exec')
    result = parse_tree(result_tree.body[0].value)

    return result
