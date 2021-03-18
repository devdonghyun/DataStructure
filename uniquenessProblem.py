import random
import time
import matplotlib.pyplot as plt


def unique_n(A):
    # code
    min_val = -len(A)
    max_val = len(A)
    B = [0 for _ in range(min_val, max_val+1)]

    for i in range(len(A)):
        B[A[i]-min_val] += 1

    for i in range(len(A)):
        if B[i] > 1:
            print("NO")
            return

    print("YES")
    return


def unique_nlogn(A):
    # code
    A.sort()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
    return


def unique_n2(A):
    # code
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                print("NO")
                return
    print("YES")
    return


n_val = []
unique_n_time = []
unique_nlogn_time = []
unique_n2_time = []

for n in range(100, 20000, 1000):
    # input: 값의 개수 n
    # n = int(input())
    # -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
    A = random.sample(range(-n, n+1), n)

    n_val.append(n)

    s = time.process_time()
    unique_n(A)
    e = time.process_time()
    print("unique_n 수행시간 = ", e-s)
    unique_n_time.append(e-s)

    s = time.process_time()
    unique_nlogn(A)
    e = time.process_time()
    print("unique_nlogn 수행시간 = ", e-s)
    unique_nlogn_time.append(e-s)

    s = time.process_time()
    unique_n2(A)
    e = time.process_time()
    print("unique_n2 수행시간 = ", e-s)
    unique_n2_time.append(e-s)

    # 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
    # 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
    # 동시에 각 함수의 실행 시간을 측정해본다
    # 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다

plt.plot(n_val, unique_n_time, 'r', label="unique_n")
plt.plot(n_val, unique_nlogn_time, 'g', label="unique_nlogn")
plt.plot(n_val, unique_n2_time, 'b', label="unique_n2")
plt.legend(loc="upper left")
plt.show()
