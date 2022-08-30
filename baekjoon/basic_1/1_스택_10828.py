import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    now = sys.stdin.readline().rstrip().split(" ")

    if now[0] == 'push':
        array.append(now[1])
    elif now[0] == 'pop':
        print(array.pop() if array else -1)
    elif now[0] == 'size':
        print(len(array))
    elif now[0] == 'empty':
        print(0 if array else 1)
    else:
        print(array[-1] if array else -1)
