% Facts about birds and their ability to fly
can_fly(eagle).
can_fly(sparrow).
can_fly(parrot).
can_fly(ostrich):- fail.  % Ostriches can't fly
can_fly(penguin):- fail.  % Penguins can't fly

% Rule to check if a bird can fly
bird_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.

bird_can_fly(Bird) :-
    \+ can_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.
