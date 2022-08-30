# 전보 (p.262)
"""
<test case>
3 2 1
1 2 4
1 3 2
>> 2 4
"""
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


INF = int(1e9)

# n : 도시 개수 / m : 통로 개수 / sender : 전송 시작 도시 (통로는 일방향)
n, m, sender = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

revise_distance = dijkstra(sender)

c, t = 0, 0
for i in range(1, n + 1):
    if i == sender:
        continue

    if revise_distance[i] < INF:
        c += 1
        t = max(t, revise_distance[i])

print(c, t)
