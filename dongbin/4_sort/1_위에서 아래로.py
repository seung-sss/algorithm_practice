# 위에서 아래로 (p.178)
"""
<test case>
3
15
27
12
>> 27 15 12
"""
n = int(input())
arr = [int(input()) for _ in range(n)]

print(*sorted(arr, reverse=True))