# data structure + algorithm => code
# but every HW/SW env different so
# virtual machine + pseudo language + psuedo code is needed
# to evelauate objectively

# virtual machine -> RAM(Random Access Machine)
# cpu + memory + basic operation

# basic operation 1 hour
# 배정, 대입, 복사
# 산술: +, -, *, / (올림, 내림, 반올림)은 원래 아니지만 ram에서 하지만 가정
# 비교: >,>=,<=,< (a-b>0)
# 논리: and, or, not
# 비트: |,&,^

# pseudo language
# 비교: if, else,if-else
# 반복: for, while
# 함수

# pseudo code
# algorithm array_max(a,n):
#     currentmax = a[0]
#     for i = 1 to n-1 do
#         if currentmax < a[i]
#     return currentmax

# time complexity
# finding average is impossible
# worstcas input -> worst time complexity
# wtc >= every case

# algorithm array_max(a,n):
#     currentmax = a[0]         -> 1
#     for i = 1 to n-1 do       -> (1 + 1) * 2 *(n-1)
#         if currentmax < a[i]  -> 1
#         currentmax = a[i]     -> 1
#     return currentmax
# wtc1 = 2n - 1

# algotithm sum(a, n):
#     sum = 0
#     for i = 1 to n-1 do:
#         if a[i] % 2 == 0:
#             sum = sum + a[i]
#     return sum
# wt2 = 4n + 1

# algotithm sum(a, n):
#     sum = 0
#     for i = 1 to n-1 do:
#         for j = i to n-1
#         sum = sum + a[i] * a[j]
#     return sum
# wtc3 = 3/2n**2 + 3/2n + 1

# Big - O
# wtc1 = 2n - 1
# wtc2 = 4n + 1
# wtc3 = 3/2n**2 + 3/2n + 1
# 최고차항이 증가율을 알려준다.
# wtc3> wtc2 == wtc1
# O(n**2) > O(n) == O(n)
