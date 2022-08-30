# 암호 만들기 (p.486)
"""
조합을 이용해 가능한 모든 경우의 수를 출력
조건 1) 적어도 1개의 모음이 들어있다
조건 2) 적어도 2개의 자음이 들어있다
-> 조건을 만족한다면, 해당 조합을 정렬해서 출력

<test case>
4 6
a t c i s w
"""
# from itertools import combinations
#
# l, c = map(int, input().split())
# char = input().split() # 가능한 암호를 사전식으로 출력하기 위해 입력 이후 정렬 수행하면 good
# result = []
#
# mo = {'a', 'e', 'i', 'o', 'u'} # 모음 = vowels
#
# for c in combinations(char, l):
#     set_c = set(c)
#
#     if len(set_c & mo) >= 1 and len(set_c - mo) >= 2:
#         result.append("".join(sorted(list(c))))
#
# for r in sorted(result):
#     print(r)


# 책 코드
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
array = input().split()
array.sort()

# 길이가 l인 모든 암호 조합을 확인
for password in combinations(array, l):
    # 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels: # vowels를 set으로 만들어 놓으면, O(1)의 시간 복잡도로 탐색 가능 (리스트는 O(N)의 사간 복잡도)
            count += 1

    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))
