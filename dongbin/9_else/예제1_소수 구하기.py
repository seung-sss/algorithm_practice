# 소수 구하기 (p.485)
"""
<test case>
3 16
>> 3
   5
   7
   11
   13
"""
import math

m, n = map(int, input().split())
array = [True] * (n + 1)
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        for j in range(i * 2, n + 1, i):
            array[j] = False

for i in range(m, n + 1):
    if array[i]:
        print(i)

# print(*[i for i in range(m, n + 1) if array[i]])

