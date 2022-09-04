print("Student Marksheet")

math = input("Enter Math Marks :- ")
urdu = input("Enter Urdu Marks :- ")
English = input("Enter English Marks :- ")
comp = input("Enter Computer Marks :- ")
Bio = input("Enter Biology Marks :- ")

math = int(math)
urdu = int(urdu)
English = int(English)
comp = int(comp)
Bio = int(Bio)

obtained_marks = math + urdu +English + comp + Bio
obtained_marks = int(obtained_marks)

percentage = obtained_marks * 100 / 500
percentage = int(percentage)
print(percentage)

if(percentage >= 90):
    print("Grade: A")
elif(percentage >= 80 & percentage < 90):
    print("Grade: B")
elif(percentage >= 70 & percentage < 80):
    print("Grade: C")
elif(percentage >= 60 & percentage < 70):
    print("Grade: D")
else:
    print("Grade: F")