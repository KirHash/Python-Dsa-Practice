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

