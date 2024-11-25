% Declare the at/2 predicate as dynamic so it can be modified
:- dynamic at/2.

% Initial Facts
at(monkey, ground).      % Monkey starts on the ground
at(box, ground).         % Box starts on the ground
at(banana, high_shelf).  % Banana is on the high shelf

% Rules
% Push the box to the shelf
push(Box) :-
    at(Box, ground),      % Box must be on the ground
    retract(at(Box, ground)),
    assert(at(Box, shelf)).

% Climb the box
climb :-
    at(box, shelf),       % Box must be on the shelf
    retract(at(monkey, ground)),
    assert(at(monkey, box)).

% Reach the banana
reach_banana :-
    at(monkey, box),      % Monkey must be on the box
    at(banana, high_shelf),
    write('Monkey got the banana!'), nl.

% Plan to get the banana: push the box, climb the box, then reach the banana
get_banana :-
    push(box),            % Push the box to the shelf
    climb,                % Climb the box
    reach_banana.         % Reach the banana
