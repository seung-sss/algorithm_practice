# 커서를 기준으로 left, right를 나눠서 다룬다 (right는 reverse)
# 커서 왼쪽 이동 => left.pop()을 right.append()
# 커서 오른쪽 이동 => right.pop()을 left.append()
# 삭제 => left.pop()
# 삽입 => left.append()

import sys

left = list(sys.stdin.readline().rstrip())
right = []

n = len(left)
m = int(sys.stdin.readline())

for _ in range(m):
    now = sys.stdin.readline().rstrip().split(' ')

    if now[0] == 'L':
        if left:
            right.append(left.pop())
    elif now[0] == 'D':
        if right:
            left.append(right.pop())
    elif now[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(now[1])

print("".join(left + right[::-1]))