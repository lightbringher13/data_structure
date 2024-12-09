# "__name__" is a special variable
# if the script is executed directly then __name__ is "__main__"
# if the script is improted. __name__ is file name

# To Control Execution: not executing functions and only print func
import demo
print("this is main.py")

# For Reusability: Allows a script to act both as a program
# and as a module that provides functionality to other scripts.
# i can use demo's display
print(demo.display("riss"))
