% Facts
parent(john, mary). parent(john, james).
parent(mary, susan). parent(mary, tom).
parent(james, lisa). parent(lisa, anna).

% Rules
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
child(X, Y) :- parent(Y, X).
ancestor(X, Y) :- parent(X, Y); (parent(X, Z), ancestor(Z, Y)).

% Queries
% ?- sibling(mary, james). % True
% ?- grandparent(john, lisa). % True
% ?- child(susan, mary). % True
% ?- ancestor(john, anna). % True
