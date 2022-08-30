# 음료수 얼려 먹기 (p.149)
"""
2차원 배열을 전체 순회한다.
0인 부분이 탐색되면, 해당 지점부터 인접한 0인 부분을 전부 1로 메꾸는 완전 탐색을 진행한다. (이후, 결과값 1씩 더하기)
이후, 위의 과정을 반복한다.

<test case>
4 5
00110
00011
11111
00000
>> 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
>> 8
"""
from collections import deque


def bfs(board, x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    q.append((nx, ny))

    return board


def dfs(x, y):
    global arr

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if arr[x][y] == 0:
        arr[x][y] = 1

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for a in range(n):
    for b in range(m):
        if arr[a][b] == 0:
            # arr = bfs(arr, a, b)
            dfs(a, b)
            result += 1

print(result)