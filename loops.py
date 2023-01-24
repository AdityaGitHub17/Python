#range(5) #--> 0,1,2,3,4

numbers = range(5)
print(numbers)   #-->will give the output as rnage(0,5)

i=0
while i<=5:
    print(i)
    i = i + 1
print("loop has finished")

j=0
while j<=5:   #-->here we cannot use i since i has updated to 5 
    print(j * '*')
    j = j + 1
print("loop has finished here")

#here for loop is generally used in some range

for i in range(5):
    print(i)
print("for loop has ended here!")    