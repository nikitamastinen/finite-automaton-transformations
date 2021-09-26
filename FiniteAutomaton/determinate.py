from typing import List, Set

from FiniteAutomaton.Edge import Edge
from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton
from queue import Queue


def hash_vertex(elements: List[str]) -> str:
    elements = [*set(elements)]
    elements.sort()
    return str(elements)


def determinate(automaton: FiniteAutomaton) -> FiniteAutomaton:
    queue: Queue[List] = Queue()
    used: Set[str] = set()
    copy = FiniteAutomaton(list(), set(), automaton.alphabet, automaton.start)

    copy.start = hash_vertex([copy.start])
    queue.put([automaton.start])
    used.add(hash_vertex([automaton.start]))

    while not queue.empty():
        vertex: List[str] = queue.get()
        used.add(hash_vertex(vertex))
        for w in automaton.alphabet:
            state: List[str] = []
            is_terminal = False
            for v in vertex:
                if v not in automaton.graph.keys():
                    continue
                for to in automaton.graph[v]:
                    if to.value == w:
                        is_terminal |= (to.end in automaton.terminals)
                        state.append(to.end)
            if len(state) >= 1:
                if hash_vertex(state) not in used:
                    queue.put(state)
                copy.add_edge(Edge(hash_vertex(vertex), hash_vertex(state), w))
                if is_terminal:
                    copy.terminals.add(hash_vertex(state))
    return copy
