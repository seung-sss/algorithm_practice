"""
쇠막대기 '('의 개수를 세어준다.
레이저 '()' 등장하면 지금까지 열린 괄호의 개수만큼 더해준다.
쇠막대기 ')'이 등장하면 +1 해주고, '('의 개수를 -1 해준다.
"""
import sys

pipe = sys.stdin.readline().rstrip().split('()')
result = 0
cnt = 0

for p in pipe:
    for i in p:
        if i == '(':
            cnt += 1
        else:
            result += 1
            cnt -= 1

    result += cnt

print(result)


# import sys
#
# N = list(sys.stdin.readline().strip().replace("()", "*"))
#
# stack = []
# result = 0
#
# for i in range(len(N)):
#     if N[i] == "(":
#         stack.append(0)
#     elif N[i] == ")":
#         stack.pop()
#         result += 1
#     else:
#         result += len(stack)
#
# print(result)