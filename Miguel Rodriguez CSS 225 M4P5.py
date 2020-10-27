#Miguel Rodriguez
#October 24,2020
#CSS 225
#Lab Activity 4

#Calculating Grades

#Write a program that will average 3 exam grades, give an average score, a letter gradde,and a message telling the student if they are passing or failing.

#Average     Grade
#90+          A
#80-89        B
#70-79        C
#60-69        D
#0-59         F

#Exams: 85,90,97
#Average: 90
#Grade: A
#Student is passing.

#Exams: 22,0,55
#Average: 26
#Grade: F
#Student is failing.

exam_one = int(input("Input of grade one exam:"))

exam_two =int(input("Input of grade two exam:"))

exam_three =int(input("Input of grade three exam:"))

average=(exam_one + exam_two + exam_three) /3
         
         if average > 90:
             letter grade = "A"
        elif average >= 80 and average < 95:
            letter_grade = "B"
        elif average >= 69 and < 79:
            letter_grade = "C"
        elif average >= 69 and average < 59:
            letter_grade = "D"
        elif average >= 59 and average < 0:
            letter_grade = "F"

print("Average:" + str(average))
print("Grade:" + letter_grade))
#I included the word "or" and also included the grade letter "D"
#This helped by knowing that if you geta "D" or lower as your grade you will fail.
if letter_grade == "F" or letter_grade == "D":
    print("Student is failing.")
else:
    print("Student is passing.")
