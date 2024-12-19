# \ to escape print
print("it\'s a lovely day ")

# """ """ you can use both ' and " for multiline string like paragraph
print(""" "it's a lovely day" """)

# \n create space
print("hello i am riss\n who are you")

# concat lines using "+", only same type
print("hello " + "i am" + " riss")

# print assignment
print("String Manipulation Exercise\nString Concatenation is done with \" + \" sign\ne.g. print(\"hello\" +_ \"riss\")\n New Lines can be created with a backslach and n")

# using , and spacing with sep
print("i", "am", "riss", sep=" | ")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# input assignment default string
print("Hey "+input("what is your name? ") + ", how are you?")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# simple variable usage, variable == pointer
# it points the address of the created object
# very important
name = input("print a number: ")
print("hell", name)

# len func use
name = input("what is the length of your name?")
print(len(name))

# swap num
a = input("enter num: ")
b = input("enter num: ")
temp = a
a = b
b = temp
print(a, b)

# variable name can have a-z,A-Z,_,0-9
# variable name can not start with 0-9
# camel case ex) myName
# pascal case ex) MyName
# snake case ex)my_name
