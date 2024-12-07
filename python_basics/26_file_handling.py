# Ram: temporary storage console
# Disk: permanent storage
# reason why file is needed
# file can be input
# file kind: txt, binary
# file operation: open read write close
# mode read: r,write: w, append: a

# create a file for write mode. it exists raise error
# f1 = open("file_1.txt", "x")

# read the file
# f1 = open("file_1.txt", "r")
# data = f1.read()
# print(data)

# write the file. no file create the file. exists overriden
# f1 = open("file_1.txt", "w")
# f1.write("Welcome to riss's world")


# r+ open the file both read and write mode. no file error
# first read and write
# f1 = open("file_1.txt", "r+")
# print(f1.tell())  # find the cursor pos
# f1.write("HI")  # cursor starts from the start overriding content
# print(f1.tell())
# print(f1.read())  # cursor goes to back. read first
# print(f1.tell())

# w+: no file create file. file exists override
# import: write mode cursor will go last so read nothing so move cursor front
# f1 = open("file_1.txt", "w+")
# print(f1.tell())
# f1.write("hi i am riss")
# print(f1.tell())
# f1.write("hi i am riss")
# print(f1.read())
# print(f1.tell())
# f1.write("hi i am riss")
# f1.seek(0)  # move cursor to front
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.close()

# append: cursor is at the end. no file create file
# f1 = open("file_1.txt", "a")
# f1.write("hello students")
# print(f1.read()) only append mode error

# a+: append and read
# f1 = open("file_1.txt", "a+")
# f1.write("love is all we need")
# f1.seek(0)
# print(f1.read())

# binary file image file
# f1 = open("image.png", "rb")
# f2 = open("image1.png", "wb")
# for i in f1: # copy the image
#     f2.write(i)
