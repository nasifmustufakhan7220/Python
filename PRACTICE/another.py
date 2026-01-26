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

month = 5
day = 4

match day :
    case 1 | 2 | 3 | 4 | 5 if month == 4 :
                print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5 :
                print("A weekday in May")
    case _ :
        print("No match")
