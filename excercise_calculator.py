from ast import operator

print("CALCULATOR")

first_number = input("Enter first Number :- ")
operator = input("Enter Operator (+,-,*,/,%,) :- ")
sec_number = input("Enter Seconds Number :- ")

first_number = int(first_number)
sec_number = int(sec_number)

if operator == '+':
    print(first_number + sec_number)
elif operator == '-':
    print(first_number - sec_number)
elif operator == '*':
    print(first_number * sec_number)
elif operator == '/':
    print(first_number / sec_number)
elif operator == '%':
    print(first_number % sec_number) 
else: 
    print("Invalid Operators")


