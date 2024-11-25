% Facts about student-teacher-subject relationships
student_teacher_subject(john, mr_smith, math101).
student_teacher_subject(mary, mr_jones, eng202).
student_teacher_subject(susan, mrs_brown, phy303).
student_teacher_subject(alex, mr_smith, cs404).

% Query to retrieve teacher and subject code based on student name
teacher_subject(Student, Teacher, SubjectCode) :-
    student_teacher_subject(Student, Teacher, SubjectCode).
