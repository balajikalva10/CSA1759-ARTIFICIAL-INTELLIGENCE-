% Check if the character is a vowel
check_vowel(X) :-
    member(X, [a, e, i, o, u]),  % Check if X is a vowel
    write('vowel'), nl.             % Print "vowel" if it is.

check_vowel(X) :-
    \+ member(X, [a, e, i, o, u]), % If X is not a vowel
    write('not vowel'), nl.         % Print "not vowel" if it is not.
