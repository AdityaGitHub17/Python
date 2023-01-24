first = input("enter the first number : ")
second = input("enter the second number : ")

sum = first + second   #-->without typeconversion
print(sum)


sum = int(first) + int(second)  #-->with typeconversion
print(sum)

#print("the sum of the given number is " + sum)  #-->wil give error we cannot concatenate the string and number

print("the sum of the given number is " + str(sum))


