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

x = "awesome" # This is a global variable. And this variable can be use anywhere in this file, both inside a function and out side a function.
def myfunc () :
    print("Python is " + x)

# myfunc()

# If we create a 