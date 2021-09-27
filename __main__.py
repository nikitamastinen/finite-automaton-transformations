from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton

if __name__ == '__main__':
    finite_automaton: FiniteAutomaton = FiniteAutomaton([
        (0, 1, 'a'),
        (1, 2, 'b'),
        (2, 2, 'a'),
        (2, 3, 'c'),
    ],
        {'1', '3'},
        ['a', 'b', 'c'],
        '0',
    )
    print(finite_automaton.get_regular_expression())
