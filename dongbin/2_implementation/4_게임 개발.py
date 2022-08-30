# 게임 개발
"""
시작 지점을 기준으로 for문을 통해 4방향을 왼쪽 방향으로 순서대로 갈 수 있는 곳인지 탐색한다. (육지이면서 방문하지 않은 곳)
-> 만일 갈 수 있는 곳이 있다면 해당 방향으로 좌표를 움직이고, 방향도 변경한다.
-> 만일 갈 수 있는 곳이 없다면 현재 지점을 기준으로 뒷 방향을 탐색한다.
    -> 뒷 방향이 육지이면 좌표를 옮기고 위의 과정을 반복한다.
    -> 뒷 방향이 바다이거나 범위를 벗어날 경우, 탐색을 종료한다.

<test case>
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
>> 3
"""
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1
result = 1

# 북동남서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    move = False
    for i in range(1, 5):
        nd = (d - i) % 4
        nx, ny = x + dx[nd], y + dy[nd]

        if 0 <= nx < n and 0 <= ny < m:
            if not graph[nx][ny] and not visited[nx][ny]:
                x, y, d = nx, ny, nd
                visited[x][y] = 1
                result += 1
                move = True
                break

    if move:
        continue
    else:
        nx, ny = x + dx[(d - 2) % 4], y + dy[(d - 2) % 4]
        if 0 <= nx < n and 0 <= ny < m:
            if not graph[x][y]:
                x, y = nx, ny
            else:
                break
        else:
            break

print(result)
# print(sum(sum(v) for v in visited))
