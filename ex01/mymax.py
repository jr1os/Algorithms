from math import inf
import time


def mymax(iteravel):
    maxi = -inf
    for i in iteravel:
        if i > maxi:
            maxi = i
    return maxi


if __name__ == "__main__":
    print(mymax([1, 2, 3, 33, 5, 6, 101]))

    print('code execution time')
    inicio = 10000
    for n in range(0, inicio * 10 + 1, inicio):
        start = time.perf_counter_ns()
        mymax(range(n))
        lasted = time.perf_counter_ns() - start
        print(lasted)
