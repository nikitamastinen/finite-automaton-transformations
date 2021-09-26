# ['1']
# ['2', '3']
# ['2', '4']
# ['2']
# ['4']
# Edges:
# ['1'] ['2', '3'] a
# ['1'] end b
# ['2', '3'] ['4'] a
# ['2', '3'] ['2', '4'] b
# ['2', '4'] ['4'] a
# ['2', '4'] ['2'] b
# ['2'] ['4'] a
# ['2'] ['2'] b
# ['4'] end a
# ['4'] end b
# Terminals:
# ['4'] ['2', '4']
# finite_automaton: FiniteAutomaton = FiniteAutomaton(
#         [
#             ('1', '2', 'a'),
#             ('1', '3', 'a'),
#             ('3', '4', 'b'),
#             ('2', '2', 'b'),
#             ('2', '4', 'a'),
#         ],
#         {'4'},
#         ['a', 'b'],
#         '1',
#     )
#     finite_automaton = determinate(finite_automaton)
#     finite_automaton = complete_edges(finite_automaton)
#     finite_automaton.print()