% Pattern matching rule to find if a sublist is in a list
sublist([], _).  % An empty list is always a sublist
sublist([X|Xs], [X|Ys]) :- sublist(Xs, Ys).  % Matching head element, then check rest of the list
sublist(Sublist, [_|Ys]) :- sublist(Sublist, Ys).  % Skip current element and check the rest

% Example query to check if a sublist exists
check_sublist :-
    sublist([2, 3], [1, 2, 3, 4, 5]),
    write('Sublist found!'), nl.

check_sublist :-
    \+ sublist([6], [1, 2, 3, 4, 5]),
    write('Sublist not found!'), nl.
