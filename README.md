# Multiple-Choice-Randomizer-and-tex-Generator
Given an input file, code randomizes the questions and associated options and prints multiple variations to a .tex file.

Input files need to be formatted in a specific manner to avoid unwanted effects.

The formatting is as follows:

Course Name and Number
Name of Exam
Time limit
Date
Number of desired forms
Number of questions

letter answer to question 1
question 1
option a for question 1
option b for question 1
option c for question 1
option d for question 1

letter answer to question 2
question 2
option a for question 2
option b for question 2
option c for question 2
option d for question 2

...

An example would be:

Math 10
Exam 2
50 minutes
October 12, 2016
3
75

c
What is 1 + 1?
0
1
2
3

d
If x = 2, what is 2 times x?
1
5
7
4

...

This piece of code does not yet handle improperly formatted input file so it is important to format correctly (i.e. no leftover carriage returns). In the above example 3 forms plus an answer highlighted form will be generated with the filename(s): Math10Exam2FormX.tex .
The answer highlighted form is Form0 whereas the rest are FormA, FormB, FormC, FormD, and so on.

This code was written with use of LaTeX in mind (with use of Pdftex personally).
Used packages are geometry and etoolbox. The document class is exam.


