% Facts (initial knowledge)
has_symptom(john, fever).
has_symptom(john, cough).

% Rules
disease(flu) :- has_symptom(_, fever).
disease(cold) :- has_symptom(_, cough).
disease(covid19) :- has_symptom(_, fever), has_symptom(_, cough).

% Forward chaining to infer a disease
infer_disease :-
    disease(Disease),
    write('Disease: '), write(Disease), nl.
