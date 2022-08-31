import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = list(map(lambda x: x[::-1], sys.stdin.readline().rstrip().split()))
    print(" ".join(sentence))

