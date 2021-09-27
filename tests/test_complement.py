from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton


def test_complement():
    finite_automaton: FiniteAutomaton = FiniteAutomaton(
        [
            ('0', '1', 'a'),
            ('1', '2', 'b'),
            ('1', '4', 'a'),
            ('2', '3', 'b'),
            ('2', '4', 'a'),
            ('3', '3', 'b'),
            ('3', '4', 'a'),
        ],
        {'2', '4'},
        ['a', 'b'],
        '1',
    )
    finite_automaton.convert_to_deterministic_automaton()

    assert finite_automaton.dict() == {
        'head': '0',
        'edges': [
            ('0', '1', 'b'),
            ('0', '3', 'a'),
            ('1', '2', 'b'),
            ('1', '3', 'a'),
            ('2', '2', 'b'),
            ('2', '3', 'a')
        ],
        'terminals': ['1', '3']
    }
