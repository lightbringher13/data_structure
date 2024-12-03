# use ",","+" for print statement
name = "riss"
age = 29
height = 1.81
print("hi i am", name, ". i am ", age, "years old.", "i am ", height, "tall")
print("hi i am "+name+". i am "+str(age) +
      " years old. i am "+str(height)+" tall.")

# use f-string much easier and can also co expressions
print(f"i am {name}. i will live until {
      age*4}years old. i will grow upto {round(height*1.02, 2)} tall")

# coding exercise
# calculate left days, months, years
age = int(input("enter your current age: "))
print(f"you have {(90-age) * 365} days, {((90-age) * 365) //
      7} weeks, {(((90-age) * 365) // 7)//5} months left")
