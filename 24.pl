% Facts: Disease-Diet relationships
diet(diabetes, low_sugar).          % Diabetics need a low-sugar diet
diet(heart_disease, low_salt).     % Heart disease patients need a low-salt diet
diet(obesity, low_calorie).        % Obesity patients need a low-calorie diet
diet(high_blood_pressure, low_sodium). % High blood pressure patients need a low-sodium diet
diet(anemia, iron_rich).           % Anemia patients need an iron-rich diet
diet(lactose_intolerance, lactose_free). % Lactose intolerant patients need a lactose-free diet

% Rule: Suggest diet based on disease
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet),
    write('For '), write(Disease), write(', you should follow a '), write(Diet), write(' diet.').

% Example Queries:
% ?- suggest_diet(diabetes, Diet).
% ?- suggest_diet(heart_disease, Diet).
% ?- suggest_diet(obesity, Diet).
% ?- suggest_diet(high_blood_pressure, Diet).
% ?- suggest_diet(anemia, Diet).
% ?- suggest_diet(lactose_intolerance, Diet).
