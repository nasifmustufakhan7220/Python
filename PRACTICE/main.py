# print("I am", 25, "years old.")
# Variable names are case sencetive. It's mean that if i create variables like these way,
age = 23
Age = 23
# print(age, Age) # Output will be ===> 23 , 23
#  these two variable are completely two different variable.

# In python, we can create and assign multiple variable in one single line. Like this way :

name, age, height = "Nasif", 25, 5.9

# print(name, age, height, sep='\n') # Output will be ====>> 
# Nasif 
# 25 
# 5.9


# Make sure one and most important thing. If we create multiple variables in one single line, we have to assign same number of values, other ways we will get an error. For example :

# name, age, height = "Nasif", 25

# print(name, age, height) # Output will show an error.


# In python we can assign same value in multiple variables in one single line. For example :

nasif_Age = srabon_Age = turjo_Age = 23
# print(nasif_Age, srabon_Age, turjo_Age, sep='\n')




# x = "awesome" # This is a global variable. And this variable can be used anywhere in this file, both inside a function and out side a function.
def myfunc () :
    print("Python is " + x)

# myfunc()
# If we create a variable outside any block or like below the x variable, it will be called as a global variable, which can be used from any where and we can use that global variable inside a block scope also. 
x = "awesome" 

def function1 () :
    # If we create a variable inside a function block or block, this variable will be local and it can not be used outside the block scope. Like below the x variable, which is only use inside that scope.
    x = "fantastic"
    print("Python is " + x)

# function1()

# print("Python is " + x)


def function2() :
    # Normally, when we carete a variable inside a function, that variable is a local variable and it can onle be used from inside a local scope, but if we use "global" keyword infornt of any variable, that varible will become a global variable and it can be used from any where in that file. Like below the varible a.
    global a
    a = "fantastic"

function2();

# print("Python is " + a)


num = 23

def numFunction () :
    # If we want to change global variable's value inside from a function scope, we can do it by using "global" keyword. Like the below code:
   global num
   num = "23"
#numFunction()
#print("My age is ", num) # output type is number.
#print("My age is " + num) # output type is string.


number = 10;

complexNum = complex(number)

print(complexNum)