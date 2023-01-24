#list is the built in datatype 

#and one more important thing in python is that in python index can be negative basically 
#here negative means from the back side

marks = [1,2,3,4,5]
print(marks) #--->will print all the element like list form only

print(marks[0]) #-->will print 1
print(marks[-1]) #-->will print 5 basically negative means it will start from the end

print(marks[0:4])#--> will print till 4(basically 4th index is not included in printing)
print(marks[0:5])#-->will print till 5(basically 5th index is not included in printing)
print(marks[1:4])#-->will print from 1st index till 3rd index

#we can use the for loop also in order to print the data

for i in marks:
    print(i)
print("loop end here!")    


#list operation

#(i) append -->add at last
marks.append(10)
print(marks)

#(ii) insert -->add at particular index ans syntax is .insert(index,value)
marks.insert(2,20)
print(marks)    #-->it does not replace the element it add and shift other element
print(20 in marks) #-->check whether 20 is present or not

print(len(marks)) ##-->tells the size of the list

#--we can traverse the the list by using the while loop
i=0
while i<len(marks):
    print(marks[i])
    i=i+1
print("while loop ends here")


#--in order to clear the list we can use the clear statement 

marks.clear()  
print(marks) #-->will print empty list


######## BREAK AND CONTINUE STATEMENT #################

name = ["gilheri","sanjhi","betu","sanjhu","chidiya","aditya","verma"]

i=0
while i<len(name):
    print(name[i])
    i = i + 1
    if name[i] == "chidiya":  #-->it will not print the chidiya 
        break    

print("while loop ends here ")


name2 = ["gilheri","sanjhi","betu","sanjhu","aditya","chidiya"]

j=0
while j<len(name2):
    if name2[j] == "aditya":
        continue
    print(name2[j])
    j=j+1
print("while loop ends here ")
  