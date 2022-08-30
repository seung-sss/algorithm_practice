# 부품 찾기 (p.197)
"""
우선 부품 리스트를 정렬한다
손님의 요청 리스트를 하나씩 이진탐색으로 탐색한다.
(계수정렬 or 집합 사용도 good)

<test case>
5
8 3 7 9 2
3
5 7 9
>> no yes yes
"""
# 1) 이진탐색 직접 구현


# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return None
#
#
# n = int(input())
# store = list(map(int, input().split()))
# m = int(input())
# require = list(map(int, input().split()))
# store.sort()
#
# for r in require:
#     if binary_search(store,r, 0, n - 1):
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")


# 이진탐색 라이브러리 사용
"""
참고 : https://velog.io/@matt2550/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%ED%95%84%EC%88%98-bisect
bisect는 target값이 없을 때, None이 아닌 현재 리스트에서 해당 값이 들어가도 순서가 깨지지 않을 위치를 인덱스값으로 돌려줌!
"""
# from bisect import bisect_left
#
# n = int(input())
# store = list(map(int, input().split()))
# m = int(input())
# require = list(map(int, input().split()))
# store.sort()
#
# for r in require:
#     # 값이 없는 경우, 들어가면 좋을 위치의 인덱스 돌려줌으로 한 번 더 검사가 필요!
#     if store[bisect_left(store, r, 0, n - 1)] == r:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")


# 계수 정렬


# n = int(input())
# store = list(map(int, input().split()))
# m = int(input())
# require = list(map(int, input().split()))
#
# array = [0] * 1000001
#
# for s in store:
#     array[s] = 1
#
# for r in require:
#     if array[r] == 1:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")


# 집합
"""
x in list => O(N)
x in set => O(1)

즉, 집합에서는 특정 원소의 존재 유무 파악할 때, 시간복잡도는 상수시간 가짐
참고 : https://velog.io/@ready2start/Python-%EC%84%B8%ED%8A%B8set%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84
"""

n = int(input())
store = set(map(int, input().split()))
m = int(input())
require = list(map(int, input().split()))

for r in require:
    if r in store:
        print('yes', end=" ")
    else:
        print('no', end=" ")