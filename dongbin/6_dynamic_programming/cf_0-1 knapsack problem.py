# knapsack problem

"""
dp를 이용한 대표적인 문제!

<fraction knapsack problem>
보석을 잘라 담을 수 있는 경우!
-> 이는 greedy로 가치 높은 애들부터 담는 방식 이용하면 됨!

<문제>
도둑이 보석가게에 배낭을 메고 침입했다.
배낭의 최대 용량은 W이며, 이를 초과해서 보석을 담으면 배낭이 찢어질 것이다.
각 보석들의 무게와 가격은 알고 있다.
배낭이 찢어지지 않는 선에서 가격 합이 최대가 되도록 보석을 담는 방법은?

[방법1 : 브루트 포스]
모든 경우의 수를 넣어보는 방법
-> But, 이는 모든 조합을 봐야하므로 최악의 시간복잡도 O(2^n)을 가짐!

[방법2 : 그리디]
가치가 가장 높은 보석부터 넣는 방법
-> But, 최적의 해를 보장하지 못함!

따라서, dp를 이용하여야 한다!

<점화식>
P[i, w] =
    1) if w_i > w => P[i - 1, w]
    -> 현재 담을 수 있는 배낭의 무게보다 현재 보석의 무게가 클 경우에는 담지 못함!
    -> 따라서 현재 배낭의 무게에서 이전 보석을 담았을 때의 값을 그대로 가져옴!

    2) else => max(v_i + P[i - 1, w - w_i], P[i - 1, w])
    -> 현재 담을 수 있는 배낭의 무게보다 현재 보석의 무게가 작거나 같은 경우에는 담을 수 있음!
    -> 따라서 이전 보석을 담았을 때의 배낭에서 현재 보석의 무게를 뺀 부분의 최대 가치에 현재 보석의 가치를 더한 값과
    -> 이전 보석을 담았을 때의 배낭에서 현재 무게에 해당하는 값과 비교하여 더 큰 것을 넣음!

참고 : https://gsmesie692.tistory.com/113
"""

# W: 배낭의 무게한도 / weight: 각 보석의 무게 / value: 각 보석의 가치 / n: 보석의 수
def knapsack_problem(W, weight, value, n):
    # DP를 위한 2차원 리스트 초기화
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weight[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j - weight[i - 1]] + value[i - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


W1 = 5
weight1 = [2, 3, 4, 5]
value1 = [3, 4, 5, 6]
n1 = 4

# 정답 : 7
print(knapsack_problem(W1, weight1, value1, n1))