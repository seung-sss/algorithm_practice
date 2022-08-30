"""
다익스트라는 '한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우'에 사용
플로이드 워셜은 '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용
-> 플로이드 워셜 알고리즘의 시간복잡도는 O(N^3)

다익스트라는 출발 노드가 1개이므로 다른 모든 노드까지의 최단 거리 저장하기 위해 1차원 리스트 사용
반면, 플로이드 워셜은 2차원 리스트에 '최단 거리' 정보를 저장함

플로이드 워셜 알고리즘은 DP 유형임!
-> 점화식 : D_ab = min(D_ab, D_ak + D_kb)
-> 내용 : 'A에서 B로 가는 최소 비용' vs 'A에서 K를 거쳐 B로 가는 비용' => 더 작은 값으로 갱신

* 다익스트라 vs 플로이드 워셜 : 메모리와 시간을 염두에 두고 알고리즘을 선택하자!
-> 노드의 개수가 적은 경우 = 플로이드 워셜
-> 노드와 간선의 개수가 모두 많은 경우 = 다익스트라
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
>> 0 4 8 6
   3 0 7 9
   5 9 0 4
   7 11 2 0
"""
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    # 만일 양방향 이동이 가능하다면, 반대인 'graph[b][a] = c'도 넣기!
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)로 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()