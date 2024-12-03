# print types
var_1 = 123
var_2 = 10.1
print(var_1 + var_2)
print(type(var_1))
print(type(var_2))
print(type(var_2 + var_1))

# print hexadecimal(16), octal(8), binary(2)
var_1 = 0o123
var_2 = 0x123
var_3 = 0b1110
print(var_1, var_2, var_3)
print(type(var_3))
print(type(var_1))
print(type(var_2))

# concat only the string type, + : only numeric values
print(123+0x123)
print("string" + "int")

# string is a list of character
str2 = "i am riss"
str1 = "will be filthy rich"
print(str2[0:4] + str1[7:])

# use \ to escape print
print("i'm \"super man\"")

# bool type
b = True
print(type(b))

# type casting and type conversion
length = len("riss")
# must have space
print("length of my name " + str(length))

# not possible
# name = "riss"
# print(10 + float(name))

# assignment
first_num = int(input("enter first_num: "))
second_num = int(input("enter second_num: "))
print("hap: ", first_num + second_num)

# assignment
two_digit = input("enter a two digit num: ")
print("hap: " + str(int(two_digit[0]) + int(two_digit[1])))
