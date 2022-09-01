# import sys
#
# s = list(sys.stdin.readline().rstrip())[::-1]
# result = ""
# special = False
# tmp = []
#
# while s:
#     now = s.pop()
#
#     if now == '<':
#         special = True
#         result += "".join(tmp[::-1])
#         result += now
#         tmp.clear()
#         continue
#
#     if now == '>':
#         special = False
#         result += now
#         continue
#
#     if special:
#         result += now
#     else:
#         if now == " ":
#             result += "".join(tmp[::-1])
#             result += now
#             tmp.clear()
#         else:
#             tmp.append(now)
#
# result += "".join(tmp[::-1])
#
# print(result)

# 풀이 참고 코드
import sys

s = list(sys.stdin.readline().rstrip())
i = 0
start = 0

while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = s[start:i]
        tmp.reverse()
        s[start:i] = tmp
    else:
        i += 1

print("".join(s))






