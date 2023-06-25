#1. it creates a  order in randomwhich the students have their oral exams (4 points),
#2. it randomly assigns every student the number of the question they will have on their oral exam (4 points),
#3. each question can be assigned only once (to one student) (4 points),
#4. the user can input the number of questions and the number of students in the class. The program
#   checks whether the number of questions is greater than the number of students and in case it is not,
#   it notifies the user (4 points),
#5. due to the possible overlapping of topics in the questions, the even- and odd-numbered questions
#   have to alternate every time (two students having an oral exams one after the other cannot both
#   have an odd- or even-numbered question. Add this feature to the final program so that it can be
#   easily commented out (only this particular part of the program) and not used (5 points).
#6. save the outcome to a text file (3 points).

import random as r

students = int(input("Input the number of students: "))
questions = int(input("Input the number of questions: "))

while questions < students:
    questions = int(input("Input the number of questions greater than number of students: "))

stud, odd, even, ques = [], [], [], []

for num in range(0, students+1):
    stud.append(str(num))

r.shuffle(stud)

def overlap():
    for num in range(1, questions+1):
        if num%2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
    r.shuffle(even)
    r.shuffle(odd)
    for num in range(len(even)-1):
        ques.append(even[num])
        ques.append(odd[num])
    return ques

def dont_overlap():
    for num in range(1, questions+1):
        ques.append(num)
    r.shuffle(ques)
    return ques

with open("students.txt", "a", encoding="utf-8") as f:
    res = overlap()
    for num in range(1, len(stud)):
        f.write(f"{num}. student: {stud[num]}, question: {res[num]}\n")
