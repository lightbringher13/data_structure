# operators
print(4/2)
print(2**3)
print(5 % 2)
print(5//3)

# assignment
bmi = 84 / (1.81 ** 2)
print(bmi)

# relational opeartors
a, b = 4, 3
c = a+b
a = a+2
c = c+a
c = c//a
print(c)
print(a == 5)
print(a < 5)
print(a >= 5)
print(c+3 != 3)

# logical opeartors
a, b = 4, 3
print((a+3 != 4) and (b == 3))
print(a or b)
print(not (a) or b)

# bitwise operator
a, b = 5, 4
print(a & b)
print(a | b)

# memorize
# ^(xor ) same: False, diff: True
print(a ^ b)
print(~a)

# memorize
# 2's = 1's + 1
# 1's change 0 t0 1 and 1 to 0
print(~b)
print(a << 2)
print(b >> 2)

# assignment
print(26 & 23)
print(17 | 24)

# memorize
# ^(xor ) same: False, diff: True
print(17 ^ 24)

# memorize
# 2's = 1's + 1
# 1's change 0 t0 1 and 1 to 0
print(~45)
print(68 << 2)
print(56 >> 3)


# identity operator
a, b = 5, 5
# id: shows memory address
# is: same address and same value
print(a is b)
print(id(a) == id(b))
print(id(a))
print(id(b))
# ==: only value
print(a == b)
b = '5'
print(a is b)
print(id(a) == id(b))
print(id(a))
print(id(b))
print(a == b)

# assignment
a = 5
print(id(a))
a = 8
print(id(a))
print(a is a)

# membership operator
s = "I am riss"
print('i' in s)
print("i " in s)
l = [23, 42, 3, 2, 1, 4, 3]
print(34 not in l)
print(42 in l)

# assignment
height = float(input("what is your height(m)? "))
weight = int(input("what is your weight(kg)? "))
bmi = weight / height ** 2
print(round(bmi, 2))
a = 3
b = "string"
print(a and b)
