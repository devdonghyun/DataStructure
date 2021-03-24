import time
import random


def prefixSum1(X, n):
    # code for prefixSum1
    for i in range(n):
        S[i] = 0
        for j in range(i):
            S[i] += X[j]


def prefixSum2(X, n):
    # code for prefixSum2
    S[0] = X[0]
    for i in range(n):
        S[i] = S[i-1] + X[i]


random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X, S = [], []
for i in range(n):
    X.append(random.randint(-n, n))

# prefixSum1 호출
prefixSum1(X, n)
# prefixSum2 호출
prefixSum2(X, n)
# 두 함수의 수행시간 출력
