# 1이 될 때까지 (P.99)
"""
n이 k로 나눠떨어질 때까지 1번 방법을 시행 (1 빼주기)
n이 k로 나눠떨어진다면 2번 방법을 시행 (k로 나눠주기)
위의 과정을 n이 1이 될 때까지 반복한다.

핵심 : 최대한 나누는 연산을 많이 시행한다
-> k가 2 이상이면 k로 나누는 것이 1을 빼는 것보다 항상 빠르게 n의 값을 줄일 수 있기 때문!!

<test case>
17 4
>> 3

25 5
>> 2
"""

n, k = map(int, input().split())
result = 0

# 단순히 순차적으로 계산하는 방법
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    result += 1

print(result)

# 개선된 방법 -> 1을 빼는 연산을 모두 수행하지 않고 한 번에 처리함으로써 효율성 향상 가능!
# while n != 1:
#     if n % k == 0:
#         n //= k
#         result += 1
#     else:
#         tmp = n % k
#         n -= tmp
#         result += tmp
#
# print(result)