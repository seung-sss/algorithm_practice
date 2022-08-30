# 1로 만들기 (p.217)
"""
<점화식>
dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3], dp[i // 5]) + 1
<test case>
26
>> 3
"""
x = int(input())
dp = [0] * (x + 1)

for i in range(2, x + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나눠 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나눠 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # 5로 나눠 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])