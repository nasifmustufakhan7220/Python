age = 32
name = "Alice Smith"
is_student = True
height = 5.7
# Converted data types

age_str = str(age);
print("Age =====>", age_str, "\n", type(age_str))

name_int = int(len(name)* 100 /2) 
print("Name =====>", name_int, "\n", type(name_int))

is_student_float = float(is_student + 5) 
print("Is Student =====>", is_student_float, "\n", type(is_student_float))

height_bool = bool(int(height));
print ("Height =====>", height_bool,"\n", type(height_bool))