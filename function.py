#there are three types of function 
    # (i)  In-built function
    # (ii) Module function
    # (iii) user defined function 

#(i)--> str(),int(),len(),bool(),max(),min(),lower(),upper() etc
#(ii)--> basically there are some module in python which has different funciton or we can also say library
        #in order to use the funciton of the library we have to import that particular module

import math
print(dir(math))#--->will print all function available in the math 

from math import sqrt #-->only import the squareroot function
print(sqrt(4))


#in order to import all function

from math import * #-->will import all the function form math
print(sqrt(81)) #-->we can use all the function


#(iii)--> user defined function
 #syntax ==>> def funciton_name(parameters):
              # code

# we will make a function which will print the sum of the two numbers              

def sum(first,second):
    print(first+second)

sum(10,12)