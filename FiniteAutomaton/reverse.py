from copy import deepcopy
from typing import Set

from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton


def reverse(determinate_automaton: FiniteAutomaton) -> FiniteAutomaton:
    automaton = deepcopy(determinate_automaton)
    automaton.add_empty_keys()
    new_terminals: Set[str] = set()
    for key in automaton.graph.keys():
        if key not in automaton.terminals:
            new_terminals.add(key)

    automaton.terminals = new_terminals
    return automaton
