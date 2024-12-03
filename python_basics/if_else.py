# # simple if else statements
# height = int(input("enter heigth: "))
# if height > 3:
#     print("buy token")
#     print("now you can board the metro")
# else:
#     print("No token required")
# print("out of block")

# # coding exercise
# # is the number is odd or even
# num = int(input("enter num: "))
# if num % 2 == 0:
#     print("num is even")
# else:
#     print("num is odd")
# print("thank you!")

# # Nested if else & elif
# height = float(input("enter your height: "))
# age = int(input("enter your age: "))
# if height > 1.65:
#     print("you can ride")
#     if age < 12:
#         print("pay 10")
#     elif age < 18:
#         print("pay 20")
#     elif age < 25:
#         print("pay 30")
#     else:
#         print("pay 45")
#     print("enjoy the ride")
# else:
#     print("sorry!, you are not tall enough")
# print("a lot more to enjoy")

# # coding exercise
# # updated bmi calculator
# weight = int(input("what is your weight: "))
# height = float(input("what is your height: "))
# bmi = weight / (height ** 2)
# print(bmi)
# if bmi < 18.5:
#     print(f"{round(bmi, 2)} underweigth")
# elif bmi <= 24.9:
#     print(f"{round(bmi, 2)} normal range")
# elif bmi <= 29.9:
#     print(f"{round(bmi, 2)} obese")
# else:
#     print("you need to lose some weight")

# # coding exercise
# # leap year or not
# year = int(input("enter a year: "))
# if year % 4 == 0:
#     print("division by 4 is 0")
#     print("maybe a leap year")
#     if year % 100 == 0:
#         print("division by 100 is 0")
#         print("maybe a leap year")
#         if year % 400 == 0:
#             print("division by 400 is 0")
#             print(f"found the leap year!! {year}")
#     else:
#         print("definitely not")
# else:
#     print("definitely not")

# # Multiple if statements
# height = float(input("enter your height: "))
# age = int(input("enter your age: "))
# bill = 0
# if height > 1.65:
#     print("you can ride")
#     if age < 12:
#         bill = bill + 10
#         print("pay 10")
#     elif age < 18:
#         bill = bill + 20
#         print("pay 20")
#     elif age < 25:
#         bill = bill + 30
#         print("pay 30")
#     else:
#         bill = bill + 45
#         print("pay 45")
#     photo = input("do you want photo?(y/n) ")
#     if photo == "y":
#         bill = bill + 5
#         print("additional 5 for the photo")
#     else:
#         print('no photo')
#     print("enjoy the ride")
# else:
#     print("sorry!, you are not tall enough")
# print(f"total bill is {bill}")

# # coding exercise
# # Pizza Order Program
# print("welcome to JaeHwan pizza shop")
# size = input("what size of pizza you want?(s,m,l)")
# bill = 0
# if size == "s":
#     bill = bill + 100
#     print(f"here is {size} pizza")
#     pepperoni = input(f"do you want pepperoni for your {size} pizza?(y/n) ")
#     if pepperoni == 'y':
#         bill = bill + 30
#         print(f"added pepperoni to your {size} pizza")
# elif size == "m":
#     bill = bill + 200
#     print(f"here is {size} pizza")
#     pepperoni = input(f"do you want pepperoni for your {size} pizza?(y/n) ")
#     if pepperoni == 'y':
#         bill = bill + 50
#         print(f"added pepperoni to your {size} pizza")
# elif size == "l":
#     bill = bill + 300
#     print(f"here is {size} pizza")
# ExtraCheese = input("do you want extra cheese?(y/n) ")
# if ExtraCheese == 'y':
#     bill = bill + 20
#     print(f"extra cheese for your {size} pizza")
# else:
#     print("you ordered wrong size")
# print(f"thank you. your total bill is {bill}")

# coding exercise
# love calculator
name1 = input("what is your name? ")
name2 = input("what is your partner's name?")

name1 = name1.lower()
name2 = name2.lower()
True_count = 0
True_count = name1.count("t") + True_count
True_count = name1.count("r") + True_count
True_count = name1.count("u") + True_count
True_count = name1.count("e") + True_count
True_count = name2.count("t") + True_count
True_count = name2.count("r") + True_count
True_count = name2.count("u") + True_count
True_count = name2.count("e") + True_count
print(True_count)
Love_count = 0
Love_count = name1.count("l") + Love_count
Love_count = name1.count("o") + Love_count
Love_count = name1.count("v") + Love_count
Love_count = name1.count("e") + Love_count
Love_count = name2.count("l") + Love_count
Love_count = name2.count("o") + Love_count
Love_count = name2.count("v") + Love_count
Love_count = name2.count("e") + Love_count
print(Love_count)
res = int(str(True_count)+str(Love_count))
if res > 90 or res < 10:
    print('best')
elif res > 40 and res < 50:
    print("soso")
else:
    print("bad")
