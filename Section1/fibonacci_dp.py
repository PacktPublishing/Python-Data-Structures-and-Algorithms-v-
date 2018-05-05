def fibonacci(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = 1

    if lookup[n] is None:
        lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup)

    return lookup[n]

if __name__ == "__main__":
    n = 5
    lookup = [None]*(n+1)

    print("Fibonacci using DP {}".format(fibonacci(n, lookup)))
