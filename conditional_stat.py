#the most important thing in python is indentation since python does not use the curly braces for the 
#conditional statement hence indentation is the most important thing to be taken care of by the programmer

a = 18
if a>=18:
    print("you are an adult ")
    print("you can give the vote ") #these both lines follows the indentation 

print("i am outside the if statement block of code") 

age = input("enter your age ")
if int(age) >=18 :
    print("you are adult ")
elif int(age)<18 and int(age)>=10:
    print("you are not adult")    
elif int(age)<10:
    print("you are too young for this")
else:
    print("enter the correct age!")    