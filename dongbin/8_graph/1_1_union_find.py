# 서로소 집합 (= union-find)
"""
서로소 집합 : 공통 원소가 없는 두 집합

서로소 집합 계산 알고리즘
1) union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    1_1) A와 B의 루트 노드 A', B'를 각각 찾는다.
    1_2) A'를 B'의 부모 노드로 설정한다. (보통 숫자가 큰 노드를 작은 노드로 연결함)
2) 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.

초기 단계에는 노드의 개수 (V) 크기의 부모 테이블을 초기화 (모든 원소가 자기 자신을 부모로 가지도록 설정)
-> 부모 테이블은 특정한 노드의 부모에 대해서만 저장하고 있음
-> 따라서 서로소 집합 알고리즘은 루트를 찾기 위해서는 재귀적으로 부모를 거슬러 올라가야 한다!

* 서로소 집합의 활용법
[무방향 그래프 내에서의 사이클 판별]
(참고로, 방향 그래프에서의 사이클 여부는 DFS를 이용하면 됨!)

union 연산은 그래프에서 간선으로 표현될 수 있음
-> 따라서 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복함으로써 사이클 판별 가능!

1) 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    1_1) 루트 노드가 서로 다르다면 두 노드에 대해 union 연산을 수행한다.
    1_2) 루트 노드가 서로 같다면  사이클(Cycle)이 발생한 것이다.
2) 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

<test case>
6 4
1 4
2 3
2 4
5 6
"""
# 1) 기본 union-find 알고리즘
# -> but, 이는 find 함수가 비효율적으로 동작하여, 최악의 경우 find 함수가 모든 노드 다 확인하며 시간 복잡도 O(V)가 걸림!


# 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x
#
#
# # 두 원소가 속한 집합을 찾기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# # v : 노드의 개수 / e : 간선의 개수
# v, e = map(int, input().split())
# parent = [0] * (v + 1) # 부모 테이블 초기화
#
# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i
#
# # union 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# # 각 원소가 속한 집합 출력
# print('각 원소가 속한 집합: ', end="")
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')
#
# print()
#
# # 부모 테이블 내용 출력
# print('부모 테이블: ', end='')
# print(*parent[1:])

# ------------------------------------------------------------------------

# 2) 개선된 union-find 알고리즘
"""
find 함수 최적화 = '경로 압축' 기법 적용
'경로 압축' : find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법

<경로 압축 소스코드>
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
경로 압축 사용함으로써 find 함수 호출한 후에, 해당 노드의 루트 노드가 바로 부모 노드가 됨!
"""


# # 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# # v : 노드의 개수 / e : 간선의 개수
# v, e = map(int, input().split())
# parent = [0] * (v + 1) # 부모 테이블 초기화
#
# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i
#
# # union 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# # 각 원소가 속한 집합 출력
# print('각 원소가 속한 집합: ', end="")
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')
#
# print()
#
# # 부모 테이블 내용 출력
# print('부모 테이블: ', end='')
# print(*parent[1:])

# ------------------------------------------------------------------------

# 3) 서로소 집합을 활용한 사이클 판별 소스코드
"""
<test case>
3 3
1 2
1 3
2 3
"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# v : 노드 개수 / e : 간선 개수
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())

    # 사이클 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')