% Facts (initial knowledge)
has_symptom(john, fever).
has_symptom(john, cough).

% Rules
disease(flu) :- has_symptom(_, fever).
disease(cold) :- has_symptom(_, cough).
disease(covid19) :- has_symptom(_, fever), has_symptom(_, cough).

% Backward chaining to check for a disease
check_disease(Patient) :-
    disease(Disease),
    write(Patient), write(' might have '), write(Disease), nl.
