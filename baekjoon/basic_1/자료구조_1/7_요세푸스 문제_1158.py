# from collections import deque
#
# n, k = map(int, input().split(' '))
# main = deque([i for i in range(1, n + 1)])
# sub = deque()
# result = []
#
# while main or sub:
#     for i in range(k):
#         if not main:
#             main, sub = sub, main
#
#         if i == k - 1:
#             result.append(main.popleft())
#         else:
#             sub.append(main.popleft())
#
# print('<' + ", ".join(map(str, result)) + '>')


# 큐 하나만 사용하여 빙글빙글 돌게 해도 될듯!!
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque([i for i in range(1, n + 1)])
result = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(str(q.popleft()))

print('<' + ", ".join(result) + '>')
