# 왕실의 나이트 (p.115)

location = input()
result = 0
x, y = ord(location[0]) - ord('a'),int(location[1]) - 1

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

for i in range(8):
    nx, ny = x + dx[i], y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        result += 1

print(result)