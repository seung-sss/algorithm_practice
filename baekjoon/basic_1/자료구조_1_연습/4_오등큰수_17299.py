"""
각 원소들의 등장 횟수를 저장한 딕셔너리 형성!
이후 오등큰수 구하는 방식 적용하기!
"""
from collections import Counter
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
result = [-1 for _ in range(len(array))]
count = Counter(array)

for i in range(len(array)):
    while stack and count[array[stack[-1]]] < count[array[i]]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)