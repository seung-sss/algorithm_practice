# 상하좌우
"""
일반적으로 1초에 2000만번 이내의 연산이면 시간 효율성 해결 가능
"""

"""
상하좌우에 대한 움직임 좌표 저장한 딕셔너리 생성한다.
이후, 주어진 명령에 따라 이동시켜 최종 좌표를 구해낸다.

시간복잡도 : 주어진 명령의 개수가 k인 경우, O(k)

<test case>
5
R R R U D D
>> 3 4
"""

n = int(input())
plan = input().split()
order = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
x, y = 0, 0

for p in plan:
    nx = x + order[p][0]
    ny = y + order[p][1]

    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny

print(x + 1, y + 1)