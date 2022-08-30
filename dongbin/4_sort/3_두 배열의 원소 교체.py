# 두 배열의 원소 교체 (p.182)
"""
tmp 리스트를 이용해 b의 원소가 a의 원소보다 큰 경우 b의 원소를 tmp에 저장
비교된 a의 원소는 삭제
이후, tmp 리스트와 a 리스트에 남은 원소들을 전부 합쳐 결과 출력

* 책 풀이
a는 오름차순, b는 내림차순으로 정렬
이후, 순차적으로 a, b 둘의 인덱스를 따라 비교하며 a < b인 경우, 둘의 원소를 교체
최대 k번 시행 후, a 리스트 원소 합 출력

<test case>
5 3
1 2 5 4 3
5 5 6 6 5
>> 26
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = []
a.sort(reverse=True)
b.sort()

for _ in range(k):
    if a[-1] < b[-1]:
        a.pop()
        tmp.append(b.pop())
    else:
        break

print(sum(tmp) + sum(a))