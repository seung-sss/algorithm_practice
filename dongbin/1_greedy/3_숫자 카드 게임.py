# 숫자 카드 게임 (p.96)
"""
각 행별로 가장 작은 숫자들을 탐색한다.
이후, 탐색된 숫자들 중 가장 큰 수를 리턴한다.

시간복잡도 : 각 행(n)에 존재하는 숫자(m)들 중 가장 작은 수를 찾는데 걸리는 시간 = O(n * m)

<test case>
3 3
3 1 2
4 1 4
2 2 2
>> 2

2 4
7 3 1 8
3 3 3 4
>> 3
"""
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    tmp = min(arr[i])
    result = max(result, tmp)

print(result)