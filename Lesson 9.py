#Prime or not Number
# def prime(num):
#     if num < 2:
#         return False
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             return False
#         i += 1
#     return True

# num = int(input())
# res = prime(num)
# print(res)

#Prime or not Series of number
# def primeSeries(num):
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             return False
#         i += 1
#     return True

# series = list(map(int,input().split()))
# for item in series:
#     ans = primeSeries(item)
#     print(item, ans)

#

# def isPrime(num):
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             return False
#         i += 1
#     return True


# k = 20
# primes = [1]*(k+1)
# prefix = [0]*(k+1)
# primes[0] = primes[1] = 0

# for i in range(2, k+1):
#     if isPrime(i):
#         primes[i] = 1
#     else:
#         primes[i] = 0
# print(primes)

 

#Sieve of Eratosthenes: While using range, primes are not calculated again and again instead it is calculated once and used again and again
# for i in range(2, k+1):
#     if primes[i] == 1:
#         j = i*i
#         while j <= k:
#             primes[j] = 0
#             j = j + i


# #Complexity:  nlog(log(n))
# print(primes)

# #Number of primes that exists before a given number
# def isPrime(num):
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             return False
#         i += 1
#     return True


# k = 20
# primes = [1]*(k+1)
# prefix = [0]*(k+1)
# primes[0] = primes[1] = 0

# for i in range(2, k+1):
#     if isPrime(i):
#         primes[i] = 1
#     else:
#         primes[i] = 0

# for i in range(2, k+1):
#     if primes[i] == 1:
#         j = i*i
#         while j <= k:
#             primes[j] = 0
#             j = j + i

# for i in range(2, k+1):
#     prefix[i] = primes[i] + prefix[i-1]

# print(prefix[5])

