#Jason Luis 
#Professor Ghaforyfard
# Februrary 19, 2024 
#Ask the student for three exam scores, Calculate the average score, and using a bunch of IF conditions, the computer should determine the grade and display the grade to the user.


#Grade Input and Calculating the Average

name = input("Student's Name: ")

grade_1 = int(input("\nWhat is your grade for Exam #1?: ")) 

grade_2 = int(input("\nWhat is your grade for Exam #2?: ")) 

grade_3 = int(input("\nWhat is your grade for Exam #3?: "))  

print("\n=======================================================================") #Border to split the input and output

average = int(grade_1 + grade_2 + grade_3) / 3  


#Grading Scale Loop

if average >= 98: 
   grade = 'A+'
elif average >= 95:
   grade = 'A'
elif average >= 91:
   grade = 'A-'
elif average >= 88: 
   grade = 'B+'
elif average >= 84: 
   grade = 'B'
elif average >= 80:
   grade = 'B-'
elif average >= 75:
   grade = 'C+'
elif average >= 70: 
   grade = 'C'
elif average < 70 and average >= 60: 
   grade = 'D'
else:
   grade = 'NC'

#Display Output
print("\nName:",name,"\n\nYour Average Score:", average, "\n\nYour Letter Grade:",grade,"\n" )

