"""
기본적인 다익스트라 알고리즘 코드는 '최단 거리가 가장 짧은 노드'를 찾기 위해 미번 최단 거리 테이블을 선형적으로 탐색함
-> 따라서, 시간복잡도 O(V^2) (V는 노드의 개수)

개선된 다익스트라 알고리즘은함 '최단 거리가 가장 짧은 노드'를 찾는 방법으로 heap 자료구조를 사용함!
-> 따라서, 최악의 경우에도 시간복잡도 O(ElogV)를 보장

파이썬에서는 우선순위 큐 사용할 때, PriorityQueue 또는 heapq를 사용!
-> 일반적으로 heapq가 더 빠르게 동작하기 때문에 heapq를 사용함!!

보통 우선순위 큐 라이브러리에 데이터 묶음(리스트, 튜픙 등)을 넣으면, 첫 번째 원소를 기준으로 우선순위 결정함!

heapq는 기본적으로 최소힙! (값이 낮은 데이터가 먼저 삭제)
-> 다익스트라에서는 최단 거리가 가장 짧은 노드를 꺼내기 때문에 그대로 사용 ok
-> 만약 최대힙 이용하고 싶으면, 우선순위 매기는 원소에 음수 부호(-)를 붙여서 넣고, 우선순위 큐에서 꺼내서 다시 음수 부호(-) 붙여 원래 값으로 돌리는 방식 사용!

<test case>
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
>> 0
   2
   3
   1
   2
   4
"""
import heapq

INF = int(1e9)

# 노드 개수, 간선 개수 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start_node = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (현재 뽑은 dist보다 최단 거리 테이블에 더 짧은 거리 갖고 있다면 이미 처리된 것!)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start_node)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)로 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])
