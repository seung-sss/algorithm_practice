# 미래 도시 (p.259)
"""
여러 장소를 들려야 하므로, 플로이드 워셜 문제!
-> n(노드 개수)이 100 이하이므로 플로이드 워셜 적용 충분함!
<test case>
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
>> 3

4 2
1 3
2 4
3 4
>> -1
"""
INF = int(1e9)

# n : 회사 개수 / m : 경로 개수
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
start = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x : 최종 도착할 위치 / k : 중간에 들릴 위치
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[start][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)


