from parsimonious.grammar import Grammar
grammar = Grammar(
    r"""
    query = subquery (lop subquery)*
    subquery = (name op val) / query / ("(" query ")")
    lop = "AND" / "OR"
    name = word
    
    op = "=" / "!=" / ">=" / "<=" / ">" / "<"
    val = number / word 
    word = " "* ~"\w+"
    number = hs? ~"[-.e\d]+" hs?
    hs = ~"[\t\ ]*"
    """)

#     subquery = (lb query rb) / (name op val)

# grammar = Grammar(
#     """
#     query = subquery
#     subquery = id op literal
#     id = ~"[A-z]*"
#     op = "=" / "!=" / ">" / "<" / ">=" / "<="
#     literal = ~"[A-z]*" / ~"[0-9]*"
#     """)


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
