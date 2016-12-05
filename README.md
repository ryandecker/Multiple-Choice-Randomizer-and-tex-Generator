# Multiple-Choice-Randomizer-and-Tex-Generator
Given an input file, code randomizes the questions and associated options and prints multiple variations to a .tex file.

In order for the software to correctly produce a .tex file, a .txt file must be in the following format:

CourseName CourseNumber
ExamTitle
TimeAllotedForExam
Date
NumberOfDesiredForms
NumberOfQuestions

AnswerToQuestion1
Question1
Option1
Option2
Option3
Option4

AnswerToQuestion2
Question2
Option1
Option2
Option3
Option4

...

and so on. The program has a built in "cleaner" to help remove non-ascii characters or to replace common characters to be more .tex friendly.
