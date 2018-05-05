def sum_recursion(n):
    pass

class Test:

    def sum_iteration(n):
        sum = 0
        for i in range(1, n+1):
            sum += i

        return sum

    def sum_recursion(n):
        if n == 1:      # Base Case
            return 1

        return n + sum_recursion(n-1)



t = Test()

print t.sum_iteration(10)

print t.sum_recursion(10)