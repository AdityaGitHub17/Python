name = "aditya verma"
print(name)
print(name.upper()) #-->does not change the original string

name2 = "SANJHI DIXIT"
print(name2)
print(name2.lower()) #-->does not change the original string

print(name.find('v'))  #indexing in python starts with zero by default
print(name.find('V'))  #if not present will print -1
print(name2.find('d'))
print(name2.find('D'))
print(name.find('verma'))  #-->we can also find the substring
print(name.find('dixit'))

name3 = "ADITYA VERMA"
print(name3.replace("VERMA","SANJHI"))#-->does not change the original string

#find funciton gives the index of the required searched element or part of the string
#but if we want to check only whether it is preseny or not then we have to use "in" function

print("A" in name3)#-->it will give true since A is present in name3
print("S" in name3)#-->it will give false since A is not present in name3
print("ADITYA" in name3)
print("ADITYA" in "ADITYA VERMA")  #-->this will also give true
