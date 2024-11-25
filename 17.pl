% Base case: The sum of first 0 digits is 0.
sum_digits(0, 0).

% Recursive case: Sum the digits from 1 to N.
sum_digits(N, Sum) :-
    N > 0,
    N1 is N - 1,                % Decrease N by 1 for recursion.
    sum_digits(N1, PartialSum), % Recursively calculate the sum of first N-1 digits.
    Sum is PartialSum + N.      % Add the current N to the partial sum.
