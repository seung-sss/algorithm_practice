# 현재 숫자까지 stack에 쌓아준다.
# 일치하는 숫자 나오면 pop한다.
# 다음 숫자가 크다면, 해당 숫자까지 쌓아주고 / 작다면, pop을 시도해본다. (pop 불일치하면 종료)
import sys

n = int(sys.stdin.readline())
result = []
stack = []
breakYN = False
i = 1

for _ in range(n):
    now = int(sys.stdin.readline())

    while i <= now:
        stack.append(i)
        i += 1
        result.append('+')

    if stack[-1] == now:
        stack.pop()
        result.append('-')
    else:
        breakYN = True
        break

if breakYN:
    print('NO')
else:
    for operation in result:
        print(operation)
