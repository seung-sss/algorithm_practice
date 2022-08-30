# 도시 분할 계획 (p.300)
"""
우선 크루스칼 알고리즘 통해 최소 신장 트리 형태로 간선을 연결함
이후, 남은 간선 중 가장 비용이 큰 간선을 제거하여 두 마을을 분리

<test case>
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
>> 8
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 비용에 따라 정렬
edges.sort()
max_cost = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)
