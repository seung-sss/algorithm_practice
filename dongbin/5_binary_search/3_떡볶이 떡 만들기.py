# 떡볶이 떡 만들기 (p.201)
"""
*파라메트릭 서치 유형 (전형적인 이진 탐색 문제)
-> 최적화 문제를 결정 문제('예' 또는 '아니오'로 답하는 문제)로 바꾸어 해결하는 기법
-> 즉, '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 사용함
-> 예를 들어 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위 좁혀갈 수 있음

따라서 해당 문제는 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정하는 것
-> '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인하고 만족 여부에 따라 탐색 범위 좁히기
-> 범위를 좁힐 때에는 이진 탐색 원리 이용하여 절반씩 범위 좁힘
(절단기 높이(탐색 범위)는 1부터 10억까지의 정수 중 하나로, 매우 큰 수이므로 이진 탐색 떠올려야 함)

<문제 해결법>
가장 긴 떡의 길이를 end 값으로 설정
mid값으로 절단기 높이 설정하고, 모든 떡을 자르고 합한 값을 계산
-> target 값보다 길이가 길다면, 절단기 높이를 키워야 함 (start값 조절)
-> target 값보다 길이가 짧다면, 절단기 높이를 줄여야 함 (end값 조절)
-> target 값과 길이가 같다면, 해당 절단기 높이를 출력
<test case>
4 6
19 15 10 17
>> 15
"""


def sum_all(array, length):
    result = 0

    for a in array:
        result += max(0, a - length)

    return result


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        tmp = sum_all(array, mid)

        if tmp == m:
            return mid
        elif tmp > target:
            start = mid + 1
        else:
            end = mid - 1

    return None


n, m = map(int, input().split())
store = list(map(int, input().split()))

print(binary_search(store, m, 0, max(store)))


# 책 코드
# n, m = map(int, input().split())
# array = list(map(int, input().split()))
#
# start = 0
# end = max(array)
#
# result = 0
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#
#     for x in array:
#         if x > mid:
#             total += (x - mid)
#
#         if total < m:
#             end = mid - 1
#         else:
#             result = mid
#             start = mid + 1
#
# print(result)
