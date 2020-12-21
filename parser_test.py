from parser_ast import parse


def test_parse_int_gt():
    assert parse('Возраст>25') == {'type': 'leaf',
                                   'op': '>',
                                   'id': 'Возраст',
                                   'literal': 25}


def test_parse_int_ge():
    assert parse('Возраст>=25') == {'type': 'leaf',
                                    'op': '>=',
                                    'id': 'Возраст',
                                    'literal': 25}


def test_parse_int_eq():
    assert parse('Возраст=25') == {'type': 'leaf',
                                   'op': '=',
                                   'id': 'Возраст',
                                   'literal': 25}


def test_parse_int_ne():
    assert parse('Возраст!=25') == {'type': 'leaf',
                                    'op': '!=',
                                    'id': 'Возраст',
                                    'literal': 25}


def test_parse_float():
    assert parse('Стаж<=.5') == {'type': 'leaf',
                                 'op': '<=',
                                 'id': 'Стаж',
                                 'literal': 0.5}


def test_parse_string():
    assert parse('Пол="М"') == {
        "op": "=",
        "id": "Пол",
        "literal": "М",
        "type": "leaf"
    }


def test_parse_age_gt_25_or_exp_ne_05():
    assert parse('Возраст>25 OR Стаж!=0.5') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": ">",
            "id": "Возраст",
            "literal": 25,
            "type": "leaf"
        },
        "right": {
            "op": "!=",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }


def test_parse_age_gt_25_and_exp_ne_05():
    assert parse('Возраст>25 AND Стаж!=0.5') == {
        "op": "AND",
        "type": "node",
        "left": {
            "op": ">",
            "id": "Возраст",
            "literal": 25,
            "type": "leaf"
        },
        "right": {
            "op": "!=",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }


def test_parse_age_gt_25_and_exp_ne_05_or_age_le_60():
    assert parse('Возраст>25 AND Стаж!=0.5 OR Возраст<=60') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": ">",
                "id": "Возраст",
                "literal": 25,
                "type": "leaf"
            },
            "right": {
                "op": "!=",
                "id": "Стаж",
                "literal": 0.5,
                "type": "leaf"
            }
        },
        "right": {
            "op": "<=",
            "id": "Возраст",
            "literal": 60,
            "type": "leaf"
        }
    }


def test_example_without_brackets_3():
    assert parse('Пол="М" AND Возраст>25 OR Стаж>.5') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "=",
                "id": "Пол",
                "literal": "М",
                "type": "leaf"
            },
            "right": {
                "op": ">",
                "id": "Возраст",
                "literal": 25,
                "type": "leaf"
            }
        },
        "right": {
            "op": ">",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }


def test_example_without_brackets_5():
    assert parse('Пол="М" AND Возраст>25 OR Стаж>.5 AND Рост=1.86 OR Имя="Вася"') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "=",
                "id": "Пол",
                "literal": "М",
                "type": "leaf"
            },
            "right": {
                "op": ">",
                "id": "Возраст",
                "literal": 25,
                "type": "leaf"
            }
        },
        "right": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": ">",
                "id": "Стаж",
                "literal": 0.5,
                "type": "leaf"
            },
            "right": {
                "op": "=",
                "id": "Рост",
                "literal": 1.86,
                "type": "leaf"
            }
        }
    }


def test_example_with_brackets_0():
    assert parse('Пол="М" AND (Возраст>25 OR Стаж>.5)') == {
        'type': 'node', 'op': 'AND',
        'left': {'type': 'leaf', 'op': '=', 'id': 'Пол', 'literal': "М"},
        'right': {
            'type': 'node', 'op': 'OR',
            'left': {'type': 'leaf', 'op': '>', 'id': 'Возраст', 'literal': 25},
            'right': {'type': 'leaf', 'op': '>', 'id': 'Стаж', 'literal': 0.5}
        }
    }


def test_example_with_brackets_1():
    assert parse('(Пол="М" AND Рост=1.86) AND (Возраст>25 OR Стаж>.5)') == {
        "op": "AND",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "=",
                "id": "Пол",
                "literal": "М",
                "type": "leaf"
            },
            "right": {
                "op": "=",
                "id": "Рост",
                "literal": 1.86,
                "type": "leaf"
            }
        },
        "right": {
            "op": "OR",
            "type": "node",
            "left": {
                "op": ">",
                "id": "Возраст",
                "literal": 25,
                "type": "leaf"
            },
            "right": {
                "op": ">",
                "id": "Стаж",
                "literal": 0.5,
                "type": "leaf"
            }
        }
    }


def test_example_with_brackets_2():
    assert parse('(Пол="М" AND Рост=1.86 AND Возраст>25 OR Стаж>.5)') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "=",
                "id": "Пол",
                "literal": "М",
                "type": "leaf"
            },
            "right": {
                "op": "=",
                "id": "Рост",
                "literal": 1.86,
                "type": "leaf"
            }
        },
        "right": {
            "op": ">",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }


def test_example_with_brackets_3():
    assert parse('((((((Пол="М" AND Рост=1.86))) AND Возраст>25 OR Стаж>.5)))') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "AND",
                "type": "node",
                "left": {
                    "op": "=",
                    "id": "Пол",
                    "literal": "М",
                    "type": "leaf"
                },
                "right": {
                    "op": "=",
                    "id": "Рост",
                    "literal": 1.86,
                    "type": "leaf"
                }
            },
            "right": {
                "op": ">",
                "id": "Возраст",
                "literal": 25,
                "type": "leaf"
            }
        },
        "right": {
            "op": ">",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }


def test_example_with_brackets_4():
    assert parse('((Пол="М" AND ((Рост=1.86) AND (Возраст>25))) OR Стаж>.5)') == {
        "op": "OR",
        "type": "node",
        "left": {
            "op": "AND",
            "type": "node",
            "left": {
                "op": "=",
                "id": "Пол",
                "literal": "М",
                "type": "leaf"
            },
            "right": {
                "op": "AND",
                "type": "node",
                "left": {
                    "op": "=",
                    "id": "Рост",
                    "literal": 1.86,
                    "type": "leaf"
                },
                "right": {
                    "op": ">",
                    "id": "Возраст",
                    "literal": 25,
                    "type": "leaf"
                }
            }
        },
        "right": {
            "op": ">",
            "id": "Стаж",
            "literal": 0.5,
            "type": "leaf"
        }
    }
