# Student Name

Name = input( "Student Name: ")

#  ID Number
IDNumber = input( "ID Number: ")

#Course
Course = input( "Course: ")

#Section
Section = input( "Section: ")

#Quarter Grades
First  = int(input( " 1st Grading: "))
Second  = int(input( " 2nd Grading: "))
Third = int(input( " 3rd Grading: "))
Fourth = int(input( " 4th Grading: "))
Average = (First + Second + Third + Fourth)




#Output

print( " Student Name: ", Name)
print( " Student ID: ", IDNumber)
print( " Course: ", Course)
print( " Section: ", Section)
print( " 1st Quarter: ", First)
print( " 2nd Quarter: ", Second)
print( " 3rd Quarter: ", Third)
print( " 4th Quarter", Fourth)
print( " Average", Average / 4)








