from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton
from FiniteAutomaton.complete_edges import complete_edges
from FiniteAutomaton.determinate import determinate
from FiniteAutomaton.reverse import reverse
from FiniteAutomaton.minimize import minimize


if __name__ == '__main__':
    finite_automaton: FiniteAutomaton = FiniteAutomaton(
        [
            (0, 1, 'a'),
            (1, 2, 'a'),
            (2, 0, 'a'),
            (3, 4, 'a'),
            (4, 5, 'a'),
            (5, 3, 'a'),
            (6, 7, 'a'),
            (7, 8, 'a'),
            (8, 6, 'a'),
            (0, 3, 'b'),
            (3, 6, 'b'),
            (6, 0, 'b'),
            (1, 4, 'b'),
            (4, 7, 'b'),
            (7, 1, 'b'),
            (2, 5, 'b'),
            (5, 8, 'b'),
            (8, 2, 'b'),
        ],
        {'0', '4', '8'},
        ['a', 'b'],
        '0',
    )
    # finite_automaton = determinate(finite_automaton)
    # finite_automaton = complete_edges(finite_automaton)
    # finite_automaton.print()
    # finite_automaton = reverse(finite_automaton)
    # finite_automaton.print()
    finite_automaton = minimize(finite_automaton)
    finite_automaton.print()
