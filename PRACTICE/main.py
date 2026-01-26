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


# number = 10;

# complexNum = complex(number)

# print(complexNum)




'''
Python can evaluate many types of values as True or False in an if statement.

Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.

This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).
'''

username = "Emil"

# if len(username) > 0 and len(username) < 10:
#     print(f"Welcome, {username}!")
# else :
#     print("Error: Username cannot be empty")


# Conditional Expression (sometimes known asa "ternary operator"): One-line if/else that prints a value

a = 2
b = 330
# print("A") if a < b else print("B")

# Assign a if/else statement into a variable : 

x = 10
b = 20

bigger = a if a > b else b
# print("Bigger is ", bigger)


# Multiple condition on One Line

x1 = 330
x2 = 330

# print("x1") if x1 > x2 else print ("=") if x1 == x2 else print ("x2")


y1 = 15
z1 = 20

max_value = y1 if y1 > z1 else z1
# print("Maximum value : ", max_value)


# Setting a default value:

Username = ""
display_name = Username if Username else "Guest"
# print("Welcome,", display_name)



# Logical Operators
# Combining Multiple Operators
'''
You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.
'''
age = 25
is_student = True
has_discount_code = False


# if (age < 18 or age > 65) and not is_student or has_discount_code :
#     print("Discount applies!")


temperature = 25
is_raining = True
is_weekend = True

# if(temperature > 20 and not is_raining) or is_weekend :
#     print("Greate day for outdoor activities!")
'''
user_name = "Tobias"
pass_word = "seceret123"
is_verified = True

 if (len(user_name) > 0 and len(pass_word) > 9 and is_verified) :
     print("Login successful")

'''
'''
user_name = "Tobias"
pass_word = "seceret123"
is_verified = True


if(len(user_name) > 0 and len(user_name) <= 6) :
    if(len(pass_word) > 8 and type(pass_word) == str) :
        if(is_verified) :
            print("Login successful")
        else :
            print("Account is not activate")
    else : 
        print("Password required")
else :
    print("Username required")


score = 92
extra_credit = 5

if score >= 90 :
    if extra_credit > 0 :
        print("A+ grade")
    else : 
        print("A grade")
elif score >= 80 :
    print("B grade")
else :
    print("C grade or below")

'''
'''
day = ""

match day :
    case 1 :
        print("Monday")
    case 2 :
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thrusday")
    case 5 :
        print("Friday")
    case 6 :
        print("Saturday")
    case 7 :
        print("Sunday")
    case _ :
        print("Error")
'''
'''
 Combine Values
 Use the pipe oprator | as an or operator in the case evaluation to check for more than one value match in one case:
'''
# day = 1

# match day :
#     case 1 | 2 | 3 | 5 :
#         print("Today is holiday")
#     case 4 | 6 :
#         print("Today is weekdays")


'''
We can also add {if} statements in the case evaluation as an extra condition-check: -
- Guards make cases unique.
- Without guards, repeating the same pattern causes an error.
- With guards, Python checks the extra condition to decide which case to run.

'''

# month = 5
# day = 4

# match day :
#     case 1 | 2 | 3 | 4 | 5 if month == 4 :
#                 print("A weekday in April")
#     case 1 | 2 | 3 | 4 | 5 if month == 5 :
#                 print("A weekday in May")
#     case _ :
#         print("No match")


'''
# FOR LOOP
'''

'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
'''
# food = ["apple", "banana", "cherry"]

# for furits in range(len(food)) :
#     print(furits) # 0, 1, 2


'''
Even strings are iterable objects, they contain a sequence of characters:
'''

# Loop through the letters in the word 
# print one by one using their length
def funcL(furits):
    x = ""
    for furit in furits :
        x += furit   
    return x

# print(funcL("banana")[2])
# for furit in range(len("banana")) :
#     print(furit)
'''
# BREAK Statement
'''

# furits = ["apple", "banana", "cherry"]

'''
break statement work after priting banana, because we write breake statement after the print function.
'''
# for x in furits :
#     print(x)
#     if x == 'banana' :
#         break
'''
 Now it will stop executting before printing banana
 '''

# for x in furits :
#     if x == "banana" :
#         break
#     print(x)

'''
# CONTINUNE 
It means that, while i use continue statement then it will not print that particular value, but if there any other values remain, it will print those values. Like below the example :
'''

# furits = ['apple', 'banana', 'cherry']

# for x in furits :
#     if x == 'banana' :
#         continue
    # print(x)

'''
range() function :

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


The range function by default start from 0 an d increments by 1 (by default), and ends at a specified number. The range function by default start from 0, however, it is possible to specify the starting value by adding a parameter : range(2,6), which means values start from 2 to 6, but not including 6.
The  range() function defaults to increament the sequence by 1, however it is possible to specify the increment value by adding a third parameter : range(2,30,3):
'''
# for x in range(2,6) :
#     print(x)

# for x in range(2,30,1) :
#     print(x)

# for x in range(1,11,2) :
#     print(x)
# else :
#     print("Finally finished")

# for x in range(1,11,2) :
#     print(x)
#     if x == 5 :
#         break
# else :
#     print("It will not excecuted")

adj = ['red', 'big', 'tasty']
furits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in furits:
        print(x,y)


