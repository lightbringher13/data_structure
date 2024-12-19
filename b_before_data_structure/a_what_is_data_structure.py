# data structure defines the relationship with data
# how the data is stored in memory
# how the operations(write, read, insert,delete, search) is done

# algorithm = finite operations to find the answer
# using data structure
# input: takes zero or more inputs
# output: produces at least one output
# finiteness: finite number of steps
# definiteness: clearly defined and unambiguous
# effectiveness: finite amount of time using basic operations.

# ex) variable
# a = 5 --> write
# print(a) --> read

# in python variable a does not store the value itself
# it stores the memory address of the object

# ex) array
# a = [3 -1 5 7]
# write, read using index
# a[3] = 3, print(a[4])
# insert
# a.append(34)
# delete
# a.pop(3),a.pop()

# gcd substract two num until one is zero
# 8: ----|----
# -
# 12: ----|----|----

# 8: ----|----
# -
# 4: ----

# 4: ----
# -
# 4: ----

# 4: ----
# -
# o

# gcd = 4

# gcd python code
def gcd_sub(a, b):
    def helper(a, b, count):
        if a == 0:
            print(f"It took {count} operations")
            return b
        if a >= b:
            return helper(a - b, b, count + 1)
        else:
            return helper(a, b - a, count + 1)

    return helper(a, b, 0)


def gcd_mod(a, b):
    def helper(a, b, count):
        if a == 0:
            print(f"It took {count} operations")
            return b
        return helper(b % a, a, count + 1)

    return helper(a, b, 0)


print(__name__)

if __name__ == "__main__":
    print(gcd_sub(1100, 2))
    print(gcd_mod(1100, 2))
