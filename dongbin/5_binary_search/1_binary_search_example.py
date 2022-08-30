"""
*tip
코딩 테스트에서 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색 가정하는 경우 많음!
-> 따라서 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제 접근해보자!!
<test case>
10 7
1 3 5 7 9 11 13 15 17 19
>> 4

10 7
1 3 5 6 9 11 13 15 17 19
>> 원소가 존재하지 않습니다.
"""


def binary_search_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)


def binary_search_simple(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n, t = map(int, input().split())
arr = list(map(int, input().split()))

# result = binary_search_recursive(arr, t, 0, n - 1)
result = binary_search_simple(arr, t, 0, n - 1)

if not result:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
