# 순열과 조합
"""
itertools 라이브러리 활용 가능!
-> permutations, combinations
"""

"""
[순열 = permutation] : 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 (nPr)
경우의 수 계산 공식 : nPr = n! / (n - r)!
"""
# import itertools
#
# data = [1, 2]
#
# for x in itertools.permutations(data, 2):
#     print(list(x))
#

"""
[조합 = combination] : 서로 다른 n개에서 "순서에 상관없이" 서로 다른 r개를 선택하는 것 (nCr)
경우의 수 계산 공식 : n! / r! x (n - r)!
"""
import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')