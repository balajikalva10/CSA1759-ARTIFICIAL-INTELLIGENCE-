% Heuristic values for nodes
state(3, a).   % Heuristic value for A is 3
state(2, b).   % Heuristic value for B is 2
state(4, c).   % Heuristic value for C is 4
state(0, goal). % Heuristic value for Goal is 0

% Compare sums of heuristic values and move accordingly
move :-
    state(HV_A, a), % Heuristic value of A
    state(HV_B, b), % Heuristic value of B
    state(HV_C, c), % Heuristic value of C

    % Calculate sums of heuristic values
    Sum_AB is HV_A + HV_B,  % Sum of A + B
    Sum_AC is HV_A + HV_C,  % Sum of A + C

    % Compare sums and move according to the smaller sum
    (Sum_AB =< Sum_AC -> Next = b; Next = c),  % If Sum_A_B is smaller or equal, move to B, otherwise move to C

    % Move to the next state
    move_to(Next).

% Move to the selected state and check if it's the goal
move_to(b) :-
    state(0, goal),  % Goal check
    write('Moved to B. Goal reached!'), nl.

move_to(c) :-
    state(0, goal),  % Goal check
    write('Moved to C. Goal reached!'), nl.

move_to(_) :-
    write('Moving to the next state. Not Goal yet!'), nl.
