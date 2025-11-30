#Q1
# name = input("Enter a name: ")
# age = int(input("Enter age: "))

# print(f"Hello {name}, you are {age} years old.")

#Q2
# a = int(input("Enter num1:"))
# b = int(input("Enter num2:"))

# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)

#Q3
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = float(input("Enter c: "))

# a1 = float(a)
# b1 = float(b)
# c1 = float(c)

# print((a1 + b1 + c1) / 3)

#Q4
# num = input("Enter a num: ")

# num1 = float(num)
# num2 = int(num)
# num3 = str(num)

# print(num1, type(num1))
# print(num2, type(num2))
# print(num3, type(num3))

#Q5
# exp = 10 + 3 * 2 ** 2
# print(exp)

#Q6
# a = int(input("enter 1st: "))
# b = int(input("enter 2nd: "))

# c = a + b
# a = c - a
# b = c - b
# print(a,b)

#Q7
# temp = input("Enter temperature in C:")

# temp1 = float(temp)

# FahrenheitTemp = (temp1*(9/5)) + 32
# print("Temp in Fahrenheit: ",FahrenheitTemp)

#Q8
# radius = int(input("Enter radius: "))

# area = 3.14*radius*radius
# print("Area is: ",area)

#Q9
# p = input("Enter principal: ")
# r = input("Enter rate of interest: ")
# t = input("Enter time in years: ")

# p1 = float(p)
# r1 = float(r)
# t1 = float(t)

# SI = (p1*r1*t1)/100

# print("Simple interest: ", SI)

#Q10
num = float(input("Enter a decimal number: "))

int_part = int(num)
frac_part = num - int_part
print("Integer part: ", int_part)
print("Fractional part: ", format(frac_part,".2f"))
