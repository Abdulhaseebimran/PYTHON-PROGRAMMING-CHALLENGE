print("ENTER YOUR AGE")

age = input("How Old are you ? :- ")
age = int(age)

if age > 18:
    print("You are adult & you can vote")

elif age < 18 and age > 5 :
    print("You are not adult & you can not vote")

else : 
    print("you are in school")

print("THANK YOU !")