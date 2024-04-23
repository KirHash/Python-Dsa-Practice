#Fibonacci

#Native Approach
# n = int(input())
# n1 = 0
# n2 = 1
# next = n2
# i = 1

# while i <= n:
#     print(next, end = ' ')
#     i += 1
#     n1, n2 = n2, next
#     next = n1 + n2
# print()

#Recursive Approach
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
res = fib(n)
print(res)