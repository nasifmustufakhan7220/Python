# The int() function in Python can convert a string to an integer only if the string represents a valid integer (in base 10 by default).
# and int() cannot directly convert a string with a decimal point
# These work:
int("25")       # → 25 (only digits)
int(" -5 ")     # → -5 (digits with optional +/- and spaces)
int("100")      # → 100 (digits only)

# These FAIL:
int("nasif")    # → ValueError (contains letters)
int("25.5")     # → ValueError (contains decimal point)
int("10 20")    # → ValueError (contains space between numbers)
int("")         # → ValueError (empty string)




age = 34
name = "John Doe"
is_student = False
height = 5.9

# Converted data types 
age_str = str(age) 
print(age_str)
print(type(age_str))

name_int = int(len(name))
print(name_int)
print(type(name_int))

is_student_int = int(is_student)
print(is_student_int)
print(type(is_student_int))

height_bool = bool(height)
print(height_bool)
print(type(height_bool))


