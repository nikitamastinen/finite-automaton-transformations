from typing import Set

from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton
from FiniteAutomaton.Edge import Edge


def remove_empty_edges(automaton: FiniteAutomaton) -> FiniteAutomaton:
    used: Set = set()
    copy = FiniteAutomaton(list(), set(), automaton.alphabet, automaton.start)

    def _dfs(v: str, root: str):
        used.add(v)

        if v not in automaton.graph.keys():
            return

        for e in automaton.graph[v]:
            if e.end in used:
                if e.end == v and e.value != '':
                    copy.add_edge(Edge(root, e.end, e.value))
                continue
            if e.value == '':
                if e.end in automaton.terminals:
                    copy.terminals.add(root)
                _dfs(e.end, root)
            else:
                copy.add_edge(Edge(root, e.end, e.value))

    for key in automaton.graph.keys():
        used.clear()
        _dfs(key, key)

    return copy
