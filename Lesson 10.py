#Recursion

#Print a Name n times
# def printNames(n):
#     if n == 0:
#         return
#     print("KirHash")
#     printNames(n-1)
# printNames(10)

# def printNames(i, n):
#     if i > n:
#         return
#     print("KirHash " + str(i))
#     printNames(i+1, n)
# printNames(1, 10)

# n = 10
# for i in range(1, n):
#     print("KirHash")
#     n -= 1

#Print 1 to n using recursion
# def printNum(i, n):
#     if i > n:
#         return
#     print(i)                      #Operation
#     printNum(i+1, n)              #Function
# printNum(1, 10)

#Print n to 1 using recursion
# def printNum(n, i):
#     if n < i:
#         return
#     print(n)                  
#     printNum(n-1, i)          
# printNum(10, 1)

# def printNum(i, n):
#     if i > n:
#         return
#     printNum(i+1, n)              #Function
#     print(i)                      #Operation
# printNum(1, 10)

#NOTE: When operation executes after function, the execution of the code reverses (as the last operation executes firstly)

#Sum of first n numbers
# n = 10
# for i in range(1, n+1):
#     sm = 0
#     if i <= n:
#         sm = sm + i
#         i += 1
# print(sm)

# def sumN(i, n, sm):
#     if i > n:
#         return sm
#     return sumN(i+1, n, sm+i)

# ans = sumN(1, 10, 0)
# print(ans)

# def sumN(i, n):
#     if i > n:
#         return 0
#     res = sumN(i+1, n) + i
#     return res

# ans = sumN(1, 5)
# print(ans)

#Factorial of a number n(in forward...1*2*3*....*n)
# n = 5
# ans = 1
# for i in range(1, n+1): 
#     ans = ans * i
# print(ans)


# def factN(i, n):
#     if i > n:
#         return 1
#     return i*factN(i+1, n)

# ans = factN(1, 5)
# print(ans)

#Factorial of a number n(in reverse...n*n-1*n-2*......*2*1)
# n = 5
# ans = 1
# for i in range(n, 0, -1):
#     ans = ans * i
# print(ans)

# def factN(n):
#     if n == 0:
#         return 1
#     return n*factN(n-1)

# res = factN(5)
# print(res)
