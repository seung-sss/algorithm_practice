import sys

n = int(sys.stdin.readline())

for _ in range(n):
    now = list(sys.stdin.readline().rstrip())
    stack = []
    breakYN = False

    for n in now:
        if n == '(':
            stack.append(n)
        if n == ')':
            if stack:
                stack.pop()
            else:
                breakYN = True
                break

    if breakYN or stack:
        print('NO')
    else:
        print('YES')
