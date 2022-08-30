# 팀 결성 (p.298)
"""
서로소 집합 알고리즘 사용!

'팀 합치기' 명령 => union을 실행
'같은 팀 여부 확인' 명령 => 두 학생의 루트 노드 찾기(find) 연산 후, 동일한지 여부 판단

<test case>
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
>> NO
   NO
   YES
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

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    # order : 0 = 팀 합치기 / 1 = 같은 팀에 속해있는지 확인
    order, a, b = map(int, input().split())

    if not order:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')