"""
https://www.hackerrank.com/challenges/fibonacci-modified
"""


def fibonacci_modified(t1, t2, n):
    # Write your code here
    dp = [0] * n
    dp[0], dp[1] = t1, t2

    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1] * dp[i - 1]

    return dp[-1]


if __name__ == '__main__':
    t1, t2, n = input().strip().split()
    t1, t2, n = int(t1), int(t2), int(n)  # type: ignore
    print(fibonacci_modified(t1, t2, n))
