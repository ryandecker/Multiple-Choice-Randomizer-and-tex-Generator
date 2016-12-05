#  author: Ryan Decker
#  email: decker.ry@gmail.com
import os
import sys
import random


class Question:
    """Question class. Has data for questions."""
    def __init__(self, f):
        self.correct_answer = []
        self.question = []
        self.options = []
        self.option_group = []
        self.gather(f)
        self.generate()

    def gather(self, f):
        """gather method. Grabs the info from file and stores it."""
        self.correct_answer = f.readline()
        self.question = f.readline()
        for i in range(4):
            self.options.append(f.readline())
        f.readline()

    def generate(self):
        """generate method. Puts the options into a tuple with a value of
        either 0 or 1. 1 means it is the correct option for that question.
        These tuples are put into a list called option_group.
        """
        answer = self.correct_answer.lower()
        temp = 0
        if answer == 'a\n':
            temp = 0
        elif answer == 'b\n':
            temp = 1
        elif answer == 'c\n':
            temp = 2
        elif answer == 'd\n':
            temp = 3
        else:  # This should not happen.
            temp = 0
        for i in range(4):
            if i == temp:
                self.option_group.append((self.options[i], 1))
            else:
                self.option_group.append((self.options[i], 0))

    def randomize(self):
        """randomize method which just shuffles the list option_group."""
        random.shuffle(self.option_group)


def print_preamble(f):
    """Prints the preamble information to file."""
    f.write('\\documentclass[10pt]{exam}\n')
    f.write('\\renewcommand\\thechoice{\\alph{choice}}\n')
    f.write('\\usepackage{geometry}\n')
    f.write('\\geometry{lmargin = 0.5in, rmargin = 0.5in, bmargin = 1in,')
    f.write('footskip = 0.3in, tmargin=1in}\n')
    f.write('\\usepackage{etoolbox}\n')
    f.write('\\patchcmd{\\choices}{\\topsep=0pt}{\\topsep=0pt\n')
    f.write('\\itemsep=0.1in}{}{}')
    f.write('\\begin{document}\n')
    f.write('\\setlength\\fillinlinelength{0.5in}\n')
    f.write('\\header{}\n')


def print_end(f):
    """Prints the ending information to file."""
    f.write('\\end{questions}\n')
    f.write('\\end{document}')


def print_all_questions(Qlist, h, f, form, ansArr):
    """Prints all of the Questions to a .tex file"""
    for i in range(h[5]):
        f.write('%'+str(i+1)+'\n')
        #  print_question(Qlist[i], f, form)
        f.write('\\begin{minipage}[c]{\\linewidth}\n')
        f.write('\\question ')
        f.write(Qlist[i].question)
        f.write('\\begin{choices}\n')
        for j in range(4):
            f.write('\\choice ')
            if Qlist[i].option_group[j][1] == 1:
                ansArr[form][i+1] = chr(65+j)
            if Qlist[i].option_group[j][1] == 1 and form == 0:
                f.write('\\textbf{')
                f.write(Qlist[i].option_group[j][0].strip())
                f.write('}\n')
            else:
                f.write(Qlist[i].option_group[j][0])
            if (j is not 3):
                f.write('\\vspace{-0.1in}\n')
        f.write('\\end{choices}\n')
        f.write('\\end{minipage}\n')
        #  f.write('\\vspace*{\\stretch{1}}\n')
        f.write('\n')


def randomize_all(Qlist, h):
    """Randomizes both the Question order and for each Question randomizes the
    order of the options.
    """
    random.shuffle(Qlist)
    for i in range(h[5]):
        Qlist[i].randomize()


def print_array(ansArr, h):
    """Prints the array with an answer sheet like format to file."""
    f_ans = open('answer_sheet.txt', 'w')
    for j in range(h[5]+1):
        if j == 0:
            f_ans.write('Form:\t')
        else:
            f_ans.write(str(j)+'\t')
        for i in range(int(h[4])+1):
            f_ans.write(str(ansArr[i][j]))
            f_ans.write('\t')
        f_ans.write('\n')
    f_ans.close()


def print_forms(Qlist, f, h):
    """Prints to multiple .tex files based on input file header info.
    Randomizes everything between writing to .tex to ensure each .tex file is
    unique.
    """
    output_files = []
    temp = []
    ansArr = [(h[5]+1)*[0] for i in range(int(h[4])+1)]
    ansArr[0][0] = '0'
    for i in range(int(h[4])):
        ansArr[i+1][0] = chr(65+i)
    temp.append(h[0].strip())
    temp.append(h[1].strip())
    prefix_name = ''.join(temp[0].split()) + ''.join(temp[1].split())
    ''' #  If I wanted to include the quarter in the filename.
    monthQuarter = {'january': 'W', 'february': 'W', 'march': 'W',
                    'april': 'Sp', 'may': 'Sp', 'june': 'Sp',
                    'july': 'Su', 'august': 'Su', 'september': 'Su',
                    'october': 'F', 'november': 'F', 'december': 'F'}
    quarter = monthQuarter[h[3].split()[0].lower()]
    year = h[3].split()[-1][-2:]
    QY = quarter + year
    prefix_name += QY'''

    for i in range(int(h[4])+1):
        if i == 0:
            output_files.append(open(prefix_name+'Form0.tex', 'w'))
        else:
            output_files.append(open(prefix_name+'Form'+chr(64+i)+'.tex', 'w'))
        print_preamble(output_files[i])
        output_files[i].write('{\\bf{' + h[0] + ' ' + h[1] + ' -- ' + h[2] +
                              '\\' + '\\' + h[3] + '}}\n')
        if i == 0:
            output_files[i].write('{\\bf{Form 0}\\\~}\n')
        else:
            output_files[i].write('{\\bf{Form '+chr(64+i)+'}\\\~}\n')
        output_files[i].write('\\vspace{.5cm}\n')
        output_files[i].write('\\begin{questions}\n')
        output_files[i].write('\n')
        print_all_questions(Qlist, h, output_files[i], i, ansArr)
        print_end(output_files[i])
        output_files[i].close()
        randomize_all(Qlist, h)
    print_array(ansArr, h)


def header_gather(h, f):
    """Grabs the important header information."""
    h.append(f.readline())
    h.append(f.readline())
    h.append(f.readline())
    h.append(f.readline())
    h.append(f.readline())
    h.append(f.readline())
    f.readline()
    h[5] = int(h[5])


def fill_question_list(Qlist, h, f):
    """Fills a list with Question objects."""
    for i in range(h[5]):
        Qlist.append(Question(f))


def clean(file_name):
    """Takes in the raw input and prepares an additional file clean_raw.txt
    for use in the rest of the code. This replaces % to \% for example.
    """
    file_name = open(file_name, 'r')
    file_lines = file_name.readlines()
    file_name.close()

    toOutput = ''
    for line in file_lines:
        for character in line:
            if character != '\r':
                toOutput += character
            else:
                toOutput += '\n'

    # underscore replacement
    underscore_check_size = 10
    for i in range(underscore_check_size):
        temp = (underscore_check_size - i)*'_'
        if temp in toOutput:
            toOutput = toOutput.replace(temp, "{\\fillin}")
    # left double quote replacement
    if u'\u201C' in toOutput:
        toOutput = toOutput.replace(u'\u201C', "``")
    # right double quote replacement
    if u'\u201D' in toOutput:
        toOutput = toOutput.replace(u'\u201D', '"')
    # apostrophe replacement
    if u'\u2019' in toOutput:
        toOutput = toOutput.replace(u'\u2019', "'")
    #  percent sign replacement
    if '\\%' in toOutput:
        toOutput = toOutput.replace('\\%', "%")
    if '\%' in toOutput:
        toOutput = toOutput.replace('\%', "%")
    if '%' in toOutput:
        toOutput = toOutput.replace('%', "\\%")

    out = open('clean_raw.txt', 'w')
    out.write(toOutput)
    out.close()


def main():
    """main. Opens the input file, grabs the header information, grabs the
    questions, and then prints the randomized questions into different output
    files.
    """
    arguments = sys.argv

    file_name = ''
    clean_name = 'clean_raw.txt'

    if len(arguments) == 2:
        file_name = arguments[1]
    else:
        file_name = 'questions_raw.txt'

    if os.path.isfile(file_name):
        clean(file_name)
        if os.path.isfile(clean_name):
            f = open(clean_name, 'rb')

            header_info = []
            question_list = []

            header_gather(header_info, f)
            fill_question_list(question_list, header_info, f)
            print_forms(question_list, f, header_info)

            f.close()
        else:
            print "Error. Cannot find clean_raw.txt"
    else:
        print "Error. Cannot find an input file."

if __name__ == '__main__':
    main()
