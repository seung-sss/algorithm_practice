# 시각
"""
보통 확인해야 할 전체 데이터 개수가 100만 개 이하일 대 완전 탐색 사용하면 적절함!
"""

"""
3중 for문으로 시, 분, 초 단위를 각각 탐색
-> 24 * 60 * 60 = 86400으로, 전체 탐색해도 충분함!

<test case>
5
>> 11475
"""
n = int(input())
result = 0

for hour in range(n + 1):
    if '3' in str(hour):
        result += (60 * 60)
        continue
    for minute in range(60):
        if '3' in str(minute):
            result += 60
            continue
        for second in range(60):
            if '3' in str(second):
                result += 1

print(result)