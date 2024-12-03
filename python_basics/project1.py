# rock paper scissors
# rock : 0, paper : 1, Scissors : 2
import random
com = random.randrange(0, 3)
user = int(input("Rock Paper Scissors Shoot!!!: "))
print(com)
# 1 0, 2 1, 0 2
if user not in [0, 1, 2]:
    print("invalud you lose")
else:
    if com == user:
        print("it is draw")
    elif (user == 1 and com == 0) or (user == 0 and com == 2) or (user == 2 and com == 1):
        print("user win")
    else:
        print("user loose")
