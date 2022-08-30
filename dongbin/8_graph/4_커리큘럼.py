# 커리큘럼 (p.303)
"""
위상정렬을 이용한다.

진입차수 담을 리스트(indegree) / 노드간 연결 정보 담은 2차원 리스트(graph) / 과목별 수강시간 담은 리스트(subject_time)
n가지의 과목들을 돌며, 해당 과목의 수강시간을 subject_time[i]에 담고, graph에서 해당 과목의 선수강 과목 부분에 해당 과목 번호(i)를 넣음
graph에 해당 과목의 선수강 과목 부분에 해당 과목 번호 넣으면서, 해당 과목의 진입차수(indegree[i])를 +1씩 해줌
위상정렬 시작
    -> 큐 생성 + 결과 담을 리스트(result)를 subject_time 복사해서 생성
    -> indegree 돌면서 진입차수 0인 과목들 큐에 넣기
    -> 큐에서 순서대로 과목 빼주고, 해당 과목에 연결된 다음 과목들의 진입차수를 -1씩 해줌
    -> 만일 다음 과목의 진입차수가 0이 되면, 현재 과목을 듣는데 걸린 시간(result[now]) + 다음 과목 듣는데 걸리는 시간(subject_time[i])으로
    -> 다음 과목을 듣는데 걸리는 최소시간(result[i])을 갱신함
    -> 이후, 다음 과목을 큐에 넣어줌

<test case>
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
>> 10
   20
   14
   18
   17
"""
from collections import deque

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
subject_time = [0]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    subject_time.append(tmp[0])

    for pre in tmp[1:-1]:
        graph[pre].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()
    result = subject_time[:]

    for i in range(n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                result[i] = result[now] + subject_time[i]
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
