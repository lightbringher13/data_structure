# after round, float type
print(round(2.6666, 2))
print(type(round(2.6666, 2)))

# after round, int type
print(round(7.555))
print(type(round(7.555)))

# tie breaking always close to even
print(round(6.5))
print(round(7.5))

# not rounded right because not stored exact in the memory
print(round(7.444445, 5))  # Output: 7.44444

# assignment
print(round(675, -1))
print(round(685, -1))
print(round(674.1012, -1))
print(round(1212, -2))
print(round(-2.5))
print(round(-3.5))
print(round(-2.6))
