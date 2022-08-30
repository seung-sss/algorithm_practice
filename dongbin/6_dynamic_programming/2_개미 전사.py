# 개미 전사 (p.220)
"""
<점화식>
dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

1) (i - 1)번째 식량창고 털기로 결정한 경우, 현재 식량창고 털 수 없다!
2) (i - 2)번째 식량창고 털기로 결정한 경우, 현재 식량창고 털 수 있다!
-> 둘 중, 더 많은 식량 털 수 있는 방법이 현재 상태에서 가장 많은 식량을 털 수 있는 경우

<test case>
4
1 3 1 5
>> 8
"""
n = int(input())
array = list(map(int, input().split()))
dp = [0] * 100

dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[n - 1])