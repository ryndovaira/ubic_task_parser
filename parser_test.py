from parser import parse


# def parse_test():
#     assert parse('Пол="М" AND (Возраст>25 OR Стаж>.5)') == {
#         'type': 'node', 'op': 'AND',
#         'left': {'type': 'leaf', 'op': '=', 'id': 'Пол', 'literal': "М"},
#         'right': {
#             'type': 'node', 'op': 'OR',
#             'left': {'type': 'leaf', 'op': '>', 'id': 'Возраст', 'literal': 25},
#             'right': {'type': 'leaf', 'op': '>', 'id': 'Стаж', 'literal': 0.5}
#         }
#     }


def test_parse_age_gt_25():
    parse('Возраст>25')


def test_parse_age_ge_25():
    parse('Возраст>=25')


def test_parse_age_eq_25():
    parse('Возраст=25')


def test_parse_age_ne_25():
    parse('Возраст!=25')


def test_parse_exp_ge_05():
    parse('Стаж<=.5')


def test_parse_age_gt_25_or_exp_ne_05():
    parse('Возраст>25 OR Стаж!=0.5')


def test_parse_age_gt_25_and_exp_ne_05():
    parse('Возраст>25 AND Стаж!=0.5')


def test_parse_age_gt_25_and_exp_ne_05_or_age_le_60():
    parse('Возраст>25 AND Стаж!=0.5 OR Возраст<=60')


def test_string_val():
    parse('Пол="М"')


def test_example_without_brackets_3():
    parse('Пол="М" AND Возраст>25 OR Стаж>.5')


def test_example_without_brackets_5():
    parse('Пол="М" AND Возраст>25 OR Стаж>.5 AND Рост=1.86 OR Имя="Вася"')


def test_example_with_brackets_0():
    parse('Пол="М" AND (Возраст>25 OR Стаж>.5)')


def test_example_with_brackets_1():
    parse('(Пол="М" AND Рост=1.86) AND (Возраст>25 OR Стаж>.5)')


def test_example_with_brackets_2():
    parse('(Пол="М" AND Рост=1.86 AND Возраст>25 OR Стаж>.5)')


def test_example_with_brackets_3():
    parse('((Пол="М" AND Рост=1.86) AND (Возраст>25 OR Стаж>.5))')


def test_example_with_brackets_4():
    parse('((((Пол="М" AND Рост=1.86) AND (Возраст>25 OR Стаж>.5))))')


def test_example_with_brackets_5():
    parse('((((((Пол="М" AND Рост=1.86))) AND ((Возраст>25 OR Стаж>.5)))))')


def test_example_with_brackets_6():
    parse('((((((Пол="М" AND Рост=1.86))) AND Возраст>25 OR Стаж>.5)))')


def test_example_with_brackets_7():
    # parse('((Пол="М" AND ((Рост=1.86) AND (Возраст>25))) OR Стаж>.5)')
    parse('(Пол="М" AND ((Рост=1.86) AND (Возраст>25))) OR Стаж>.5')
