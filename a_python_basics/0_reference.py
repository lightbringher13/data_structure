"""

immutable type:
int, float, complex, bool, str, tuple, frozenset, bytes

mutable type:
list, dict(key->immutable), set, bytearray

"""
import copy

# mutable type(list) reference


def mutable_type_reference():
    a = [1, 2, 3]  # 'a' references a list object in memory
    b = a  # 'b' is another reference to the SAME list object

    b[0] = 100  # Modify the list using 'b'

    print(a)
    print(b)
    print(id(a))
    print(id(b))

# immutable type(list) reference


def immutable_type_reference():
    a = 10
    b = a  # Both x and y reference the same integer

    b = 11  # y now references a NEW integer

    print(a)
    print(b)
    print(id(a))
    print(id(b))

# mutable type(list) create new object instead of reference


def mutable_type_create_new_object():
    a = [1, 2, 3]
    b = a.copy()  # Creates a new list (shallow copy)

    b[0] = 100  # Modifies 'b', but NOT 'a'

    print(a)
    print(b)
    print(id(a))
    print(id(b))

# mutable type(list) function arguement


def mutable_type_function_arguement(lst):
    lst.append(4)  # Modifies the original list

# mutable type(list) function arguement


def immutable_type_function_arguement(num):
    num += 100  # Creates a new integer, does not modify the original


# shallow copy


def shallow_vs_deep_copy():
    print("\nshallow copy")
    original_shallow = [[1, 2, 3], [4, 5, 6]]

    # Creates a new outer list, but inner lists are shared
    shallow_copied = copy.copy(original_shallow)

    # Modifies the first element of the first inner list
    shallow_copied[0][0] = 100

    # Output: [[100, 2, 3], [4, 5, 6]] (Original is affected!)
    print(original_shallow)
    print(shallow_copied)  # Output: [[100, 2, 3], [4, 5, 6]]

    print("\ndeep copy")
    original_deep = [[7, 8, 9], [10, 11, 12]]
    # Creates a fully independent copy
    deep_copied = copy.deepcopy(original_deep)

    # Modifies the first element of the first inner list
    deep_copied[0][0] = 100

    # Output: [[1, 2, 3], [4, 5, 6]] (Original is unchanged)
    print(original_deep)
    print(deep_copied)  # Output: [[100, 2, 3], [4, 5, 6]]


if __name__ == "__main__":
    print("mutable type reference: ")
    mutable_type_reference()

    print("\nimmutable type reference: ")
    immutable_type_reference()

    print("\nmutable type create new object: ")
    mutable_type_create_new_object()

    print("\nmutable type(list) function arguement: ")
    my_list = [1, 2, 3]
    mutable_type_function_arguement(my_list)
    print(my_list)

    print("\nimmutable type(int) function arguement: ")
    x = 10
    immutable_type_function_arguement(x)
    print(x)

    shallow_vs_deep_copy()
