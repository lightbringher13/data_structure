# simple example of for
numbers = [2, 3, 5, -2, 10]
square_numbers = []
for num in numbers:

    square_numbers.append(num ** 2)
print(square_numbers)

# for - else
# else block will execute only if for block is executed sucessfully
# sign of no - break
tuple1 = (2, 56, 34, 3, 5, -1)
for num in tuple1:
    # print(num)
    if num % 6 == 0:
        break
        print(num)
        # if num == 5:
        #     break
else:
    print("sucessfully executed!")
print("out of for/else")

# coding exercise
# calculate average height of a list of heights
heights = []
heights = input("enter heights: ")
heights = heights.split(" ")
num = 0
heights_sum = 0
for i in heights:
    num = num + 1
    heights_sum = int(i) + heights_sum
avg = round(heights_sum / num)
print(f"avg of heights: {avg}")

# coding exercise
# find the maximun number in a list
numbers = input("enter numbers: ")
numbers = numbers.split(" ")
for num in numbers:
    max = numbers[0]
    if max < num:
        max = num
print(max)
