# 시간 초과
# 현재 풀이는 O(N^2)의 시간복잡도를 가짐


# import sys
#
# n = int(sys.stdin.readline())
# array = list(map(int, sys.stdin.readline().split()))
# result = []
#
# for i in range(n):
#     now = array[i]
#     breakYN = False
#
#     for j in range(i+1, n):
#         if array[j] > now:
#             print(array[j], end=" ")
#             breakYN = True
#             break
#
#     if not breakYN:
#         print(-1, end=" ")


# O(N)의 시간복잡도 갖는 코드 만들기 -> 스택 이용
"""
왼쪽부터 순서대로 해당 인덱스를 스택에 넣어준다.
스택에 값이 있고, 스택 최상단값이 현재 넣을 값보다 작은 경우
-> 스택 최상단 pop해서, 해당 인덱스에 현재 넣을 값으로 업데이트 해준다.
이외에는 스택에 현재 넣을 값의 인덱스 넣기
"""
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
result = [-1] * len(array)

for i in range(len(array)):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)