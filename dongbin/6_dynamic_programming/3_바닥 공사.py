# 바닥 공사 (p.223)
"""
길이 1의 바닥 채우는 방법 -> 1가지
길이 2의 바닥 채우는 방법 -> 3가지
길이 3의 바닥 채우는 방법 -> (길이 1 방법) * 2가지 + (길이 2 방법) * 1가지

즉, dp[i] = dp[i - 1] + dp[i - 2] * 2

타일의 가로 길이가 최대 2이므로, (i - 2)까지만 고려!

<test case>
3
>> 5
"""
n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])