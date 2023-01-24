#---tuple is list which is immutable basically it can not allow us make any changes with the tuple

marks = (12,34,56,87,43,43,43,43)
#marks[2] = 67 #--> this will give error since tuple is immutable

#----but tuple gives us count of the number you want to check in tuple
print(marks.count(12))
print(marks.count(43)) 

# we can also find the index of the particular element
print(marks.index(43))
print(marks.index(56))