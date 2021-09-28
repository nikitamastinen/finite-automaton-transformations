# finite-automaton-transformations
A module that allows you to perform various actions with finite automatons:

## What can it do
* Remove empty-value edges
* Convert non-deterministic finite automaton to deterministic
* Add missing edges
* Complement
* Minimize
* Get regular expression

## Get started

* Build virtual environment
``` console
make venv
```
* Run tests
``` console
make test
```

## How to use
  * To import the main class **FiniteAutomaton** from root directory of project write
 ``` python
from FiniteAutomaton.FiniteAutomaton import FiniteAutomaton
```   

  * To create **FiniteAutomaton** look at this example
 ``` python
finite_automaton: FiniteAutomaton = FiniteAutomaton(
        [
            ('0', '1', 'a'),  # (from, to, word)
            ('1', '2', 'b'),
            ('1', '4', 'a'),
            ('2', '3', 'b'),
            ('2', '4', 'a'),
            ('3', '3', 'b'),
            ('3', '4', 'a'),
        ],  # dict of tuples that contains edges of finite automaton 
        {'2', '4'},  # set of terminal vertices
        ['a', 'b'],  # alphabet  
        '1',  # start vertex
    )
```
* How to call methods
 ``` python
# removes empty-value edges from current 
finite_automaton.remove_empty_value_edges(

# converts current to finite deterministic automaton
finite_automaton.convert_to_deterministic_automaton()

# adds missing edges to current
finite_automaton.add_missing_edges()

# minimize number of vertices in current
finite_automaton.minimize()

# complements current
finite_automaton.complement()

# returns regular expression that equals current finite automaton
finite_automaton.get_regular_expression()

# prints current
finite_automaton.print()

# converts current to dict
finite_automaon.dict()
```

Developed by Nikita Mastinen, 2021
