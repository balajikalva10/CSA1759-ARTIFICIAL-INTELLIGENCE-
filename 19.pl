% Facts
teacher(mr_smith, alice).
teacher(mr_smith, bob).
teacher(ms_jones, charlie).
teacher(ms_jones, diana).

% Rule to find the teacher of a student
student_teacher(Student, Teacher) :- teacher(Teacher, Student).

% Rule to find all students of a teacher
teacher_students(Teacher, Students) :- findall(Student, teacher(Teacher, Student), Students).

% Sample queries:
% ?- student_teacher(alice, Teacher).
% ?- teacher_students(mr_smith, Students).
