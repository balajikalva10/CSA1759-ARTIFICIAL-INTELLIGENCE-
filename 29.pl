% Symptoms and Diseases
% Facts representing symptoms and diseases
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(john, sore_throat).

has_symptom(mary, headache).
has_symptom(mary, fever).
has_symptom(mary, nausea).

% Diseases based on symptoms
disease(covid19) :- has_symptom(_, fever), has_symptom(_, cough), has_symptom(_, sore_throat).
disease(flu) :- has_symptom(_, fever), has_symptom(_, cough).
disease(migraine) :- has_symptom(_, headache).
disease(gastroenteritis) :- has_symptom(_, nausea), has_symptom(_, fever).

% Diagnosis rule
diagnose(Patient) :-
    disease(Disease),
    write(Patient), write(' is diagnosed with '), write(Disease), nl.

% Query the diagnosis for a patient
query_diagnosis(Patient) :-
    (diagnose(Patient) -> true; write('No diagnosis found for '), write(Patient), nl).
