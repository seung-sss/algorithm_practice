# 성적이 낮은 순서로 학생 출력하기 (p.180)
"""
<test case>
2
홍길동 95
이순신 77
>> 이순신 홍길동
"""
n = int(input())
score = []

for _ in range(n):
    tmp = input().split()
    score.append([tmp[0], int(tmp[1])])

score.sort(key=lambda x: x[1])
print(*[x[0] for x in score])