from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    now = sys.stdin.readline().rstrip().split(' ')

    if now[0] == 'push_front':
        q.appendleft(now[1])
    elif now[0] == 'push_back':
        q.append(now[1])
    elif now[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif now[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif now[0] == 'size':
        print(len(q))
    elif now[0] == 'empty':
        print(0 if q else 1)
    elif now[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)