from copy import deepcopy

from FiniteAutomaton.Edge import Edge
from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton


def complete_edges(determinate_automaton: FiniteAutomaton) -> FiniteAutomaton:
    automaton = deepcopy(determinate_automaton)
    automaton.add_empty_keys()

    if 'end' in automaton.graph.keys():
        print('Sorry "end" is reserved word, use another to name your automaton vertices')
        raise Exception()

    last_name = 'end'
    old_keys = deepcopy([*automaton.graph.keys()])
    for key in old_keys:
        for w in automaton.alphabet:
            is_value_founded: bool = False
            for edge in automaton.graph[key]:
                if edge.value == w:
                    is_value_founded = True
            if not is_value_founded:
                automaton.add_edge(Edge(key, last_name, w))
    automaton.reindex_vertices()
    return automaton
