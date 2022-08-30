# 큰 수의 법칙 (p.92)
"""
주어진 배열을 정렬하여 가장 큰 수와 두번 째로 큰 수를 찾아낸다
이후 가장 큰 수를 k번 더하고, 두번 째로 큰 수를 한 번 더하는 과정을 총 m번이 될 때까지 시행한다.

<test case>
5 8 3
2 4 5 4 6
>> 46
"""

"""
<test>
Q. sort를 사용할 때, reverse를 함께 사용한다면 시간이 더 걸릴까?
A. 유의미한 차이는 없는 것으로 확인됨
"""
# import random
# import time
#
# a = []
#
# for i in range(100000):
#     a.append(random.randrange(0, 10000))
#
# s_time = time.time()
# a.sort()
# e_time = time.time()
#
# print(f"단순 정렬 : {e_time - s_time}")
#
# b = []
#
# for i in range(100000):
#     b.append(random.randrange(0, 10000))
#
# s_time = time.time()
# b.sort(reverse=True)
# e_time = time.time()
#
# print(f"단순 정렬 뒤집기 : {e_time - s_time}")


n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort(reverse=True)

# 1) 단순하게 반복적으로 더하는 방법
# for i in range(1, m + 1):
#     if i % (k + 1) == 0:
#         result += arr[1]
#     else:
#         result += arr[0]
#
# print(result)

# 2) 한 번의 수학적 계산으로 더하는 방법
result = ((arr[0] * k) + arr[1]) * (m // (k + 1)) + (arr[0] * (m % (k + 1)))

print(result)


