% Facts: Example state space and heuristic values
% state(Heuristic, State)
state(2, start).
state(1, a).
state(3, b).
state(0, goal).

% Define the transitions (edges between states)
transition(start, a).
transition(start, b).
transition(a, goal).
transition(b, goal).

% Best First Search algorithm
best_first_search(Start, Goal) :-
    best_first_search([Start], Goal, [Start]).

% Base case: Found the goal
best_first_search([Goal|_], Goal, _) :-
    write('Goal found: '), write(Goal), nl.

% Recursive case: Expand nodes based on heuristic values
best_first_search(OpenList, Goal, ClosedList) :-
    OpenList = [CurrentState|Rest],
    find_neighbors(CurrentState, Rest, Goal, Neighbors),
    append(Neighbors, Rest, NewOpenList),
    sort(2, @=<, NewOpenList, SortedOpenList), % Sort by heuristic values
    best_first_search(SortedOpenList, Goal, [CurrentState|ClosedList]).

% Find neighboring states (direct transitions)
find_neighbors(CurrentState, Rest, Goal, Neighbors) :-
    findall(Neighbor, (transition(CurrentState, Neighbor), \+ member(Neighbor, Rest)), Neighbors).

% Query: Find the best first search from start to goal
