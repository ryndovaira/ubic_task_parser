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
