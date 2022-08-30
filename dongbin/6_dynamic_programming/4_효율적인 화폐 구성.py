# 효율적인 화폐 구성 (p.226)
"""
dp테이블을 10001(해당 액수를 만들 수 없는 경우를 의미)로 초기화
0원을 만들 수 있는 화폐 개수는 0이므로, dp[0] = 0으로 지정

이후, 모든 지폐 종류를 for문으로 돈다
-> 각 지폐 종류마다 해당 지폐 액수부터 m원까지 dp테이블을 채움
-> (현재 액수에서 현재 지폐 크기를 뺀 경우의 지폐 개수 + 1 vs 현재 액수에서의 지폐 개수) 중 작은 값

<test case>
2 15
2
3
>> 5

3 4
3
5
7
>> -1
"""
n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
        # if dp[j - money[i]] != 10001:
        #     dp[j] = min(dp[j], dp[j - money[i]] + 1)
        dp[j] = min(dp[j], dp[j - money[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])