# character to number
# ord(), The term “ordinal” refers to the position or rank of a character in the Unicode or ASCII table.
import random
char = 'a'
print(ord(char))
char = 'z'
print(ord(char))
char = "A"
print(ord(char))
char = "Z"
print(ord(char))

# number to character
# chr(), The term “character” refers to a single symbol represented by a Unicode code point.
number = 97
print(chr(number))
number = 122
print(chr(number))
number = 65
print(chr(number))
number = 90
print(chr(number))

letters = []
for i in range(97, 123):
    letters.append(chr(i))
for i in range(65, 91):
    letters.append(chr(i))
print(letters)

symbols = []
for i in range(33, 48):
    symbols.append(chr(i))
print(symbols)

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

print("welcome to the Password Generator")
letters_num = int(input("how many letters would you like in your passoword?"))
numbers_num = int(input("how many numbers would you like in your passoword?"))
symbols_num = int(input("how many symbols would you like in your passoword?"))

# random.sample(origin,3) randomly select 3 from origin without duplicates
# random.choices(origin,3) randomly select 3 from origin with duplicates
letters_selected = random.sample(letters, int(letters_num))
numbers_selected = random.sample(numbers, int(numbers_num))
symbols_selected = random.sample(symbols, int(symbols_num))

password = letters_selected + numbers_selected + symbols_selected
print(password)
random.shuffle(password)
print(password)

# put list elements into string
final_pw = ""
for char in password:
    final_pw = final_pw + str(char)
print(final_pw)

# another way of list to string
print("".join(final_pw))
