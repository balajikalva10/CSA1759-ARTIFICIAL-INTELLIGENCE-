% Facts about persons and their DOB
person(john, '1990-01-01').
person(mary, '1985-05-15').
person(susan, '1992-07-30').
person(alex, '1980-11-20').

dob(Name, DOB) :-
    person(Name, DOB).
