# modules ex) math, pandas...
# why module? reusablility, organization
# very large project should be divided.
import math
from my_module import QuizGame
from my_module import *
import my_module
# print(help("math"))
# print(math.e)
# q = QuizGame()
# q.play()
a = 11
print(a)
print(my_module.a)  # avoid conflict
