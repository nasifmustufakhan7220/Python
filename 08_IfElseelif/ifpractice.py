# num = int(input("Enter a number: "))
# sign= input("Enter the sign (+ / - / * / ÷) to calculate the two numbers: ")
# num1 = int(input("Enter another number: "))

# sum = 0

# if (sign == "+") :
#     sum = num + num1
#     print("The addition of the two numbers is : ", sum)
# elif(sign == "-") :
#     sum = num - num1
#     print("The subtraction of the two numbers is : ", sum)
# elif(sign == "*") :
#     sum = num * num1
#     print("The multiplication of the two numbers is : ", sum)
# elif(sign == "/") :
#     sum = num / num1
#     print("The division of the two numbers is : ", sum)
# else :
#     print("You're result is invalid")



bng = int(input("Enter your Bangla marks: "))
eng = int(input("Enter your English marks: "))
math = int(input("Enter your Math marks: "))
scn = int(input("Enter your Science marks: "))
isl = int(input("Enter your Islam marks: "))

total = bng + eng + math + scn + isl
avg = total / 5
print(avg)


if(avg >= 90 and avg <=100) :
    grade = "A+"
    print("Congratulations! You got", f"{grade}" )
elif(avg >= 80 and avg <90) :
    grade = "A"
    print("Congratulations! You got", f"{grade}" )
elif(avg >= 70 and avg < 80) :
    grade = "B"
    print("Congratulations! You got", f"{grade}")
elif(avg >= 60 and avg < 70) :
    grade = "C"
    print("Congratulations! You got", f"{grade}")
elif(avg>= 50 and avg < 60) :
    grade = "D"
    print("Congratulations! You got", f"{grade}")
else :
    grade = "F"
    print("You have to doing hard work! Other ways you will be kick out from the university")