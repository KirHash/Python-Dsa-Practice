# Patterns


# Pattern 1
# n = 5
# for i in range(n):
#     for j in range(n):  
#         print("*", end="")
#     print("*")

# Pattern 2
# n = 5
# for i in range(n):
#     for j in range(i):
#         print("*", end="")
#     print("*")

# Pattern 3
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(j+1, end="")
#     print(i+1)

# Pattern 4
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(i+1, end="")
#     print(i+1)

# Pattern 5
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# Pattern 6
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(j+1, end="")
#     print()

# Pattern 7
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("*", end="")
#     print()

#Pattern 8
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(2*(n-i-1)+1):
#         print("*", end="")
#     print()

# Pattern 9
# n = 5
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("*", end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(2*(n-i-1)+1):
#         print("*", end="")
#     print()


# Pattern 10
# n = 5
# for i in range(n):
#     for j in range(i):
#         print("*", end="")
#     for k in range(n-i):
#         print(" ", end="")
#     print()
# for i in range(n+1):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# Pattern 11
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if (i+j)%2 == 0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()

# Pattern 12
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end="")

#     for j in range((n-1-i)*2):
#         print(" ", end="")
    
#     for j in range(i+1,0,-1):
#         print(j, end="")
#     print()

# Pattern 13
# n = 5
# k = 1
# for i in range(n):
#     for j in range(i+1):
#         print(k, end=" ")
#         k += 1
#     print()
        
# Pattern 14
# def numToChr(num):
#     return chr(num+65)

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(numToChr(j), end="")
#     print()

# Pattern 15
# def numToChr(num):
#     return chr(num+65)

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(numToChr(j), end="")
#     print()

# Pattern 16
# def numToChr(num):
#     return chr(num+65)

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(numToChr(i), end="")
#     print()

# Pattern 17
# def numToChr(num):
#     return chr(num+65)

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i):
#         print(numToChr(j), end="")
#     for j in range(i,-1,-1):
#         print(numToChr(j), end="")
#     print()

# Pattern 18
# def numToChr(num):
#     return chr(num+65)

# n = 5
# k = n-1
# for i in range(n):
#     for j in range(i+1):
#         print(numToChr(k+j), end="")
#     k -=1
#     print()

# n = 5
# for i in range(n+1):
#     if i % 2 == 0:
#         for j in range(i, 0, -1):
#             print(j, end="")
#     else:
#         for j in range(1, i+1):
#             print(j, end="")
#     print()




        

