from parser import parse


def parse_test():
    assert parse('Пол="М" AND (Возраст>25 OR Стаж>.5)') == {
        'type': 'node', 'op': 'AND',
        'left': {'type': 'leaf', 'op': '=', 'id': 'Пол', 'literal': "М"},
        'right': {
            'type': 'node', 'op': 'OR',
            'left': {'type': 'leaf', 'op': '>', 'id': 'Возраст', 'literal': 25},
            'right': {'type': 'leaf', 'op': '>', 'id': 'Стаж', 'literal': 0.5}
        }
    }


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

def test_parse_age_gt_25_or_exp_gt_05():
    parse('Возраст>25 OR Возраст!=25')
