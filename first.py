print("hello world")

name = "aditya" #here we dont need to define the datatype of the variable
age = 21  #python itself can determine the datatype of the variable

print("name")
print(name)
print(age)

age = 24
print(name)
print(age)

print("i am " + name)
#print("my age is" + age)--> this wil error it can only concatenate the string


newage = input("enter you age ")  #--> here the python is taking as a string not as int
print("your age is ")
print(newage)

#oldage = newage - 2   #-->here newage is string and 2 is an integer so it will not concatenate
#print(oldage)  #-->this will give error above line has error

#now in order to resolve this problem we need to do typeconversion

oldage = int(newage) - 2
print(oldage)  #-->now it will not give any error


#now similarly we can use different type conversion
#str()  , float() , bool() etc

