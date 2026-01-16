# Decleare variable then assign values.
age = input("Age : ", )
name = input("Name : ")
height = input("Height : ")
cgpa = input("CGPA : ")

# Converting data type from one type to another

age_float = float(int(age))
print("Age : " , age_float)

name_int = int(len(name))
print("Name : " , name_int)

height_int = int(float(height))
print("Height : " , height_int)

cgpa_bool = bool(float(cgpa))
print("CGPA : " , cgpa_bool)

