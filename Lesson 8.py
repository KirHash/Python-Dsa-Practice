# Basic Maths Problems

# Count Digits
# def countDigit(num):
#     count = 0
#     while num > 0:
#         num = num//10
#         count += 1
#     return count

# num = int(input())
# ans = countDigit(num)
# print(ans)

# Reverse Number
# def revNum(num):
#     ans = 0
#     while num > 0:
#         rev = num%10
#         ans = ans*10 + rev
#         num = num//10
#     return ans
# num = int(input())
# ans = revNum(num)
# print(ans)

#Pallindrome
# def revNum(num):
#     ans = 0
#     while num > 0:
#         rev = num%10
#         ans = ans*10 + rev
#         num = num//10
#     return ans

# def pallindrome(num):
#     return num == revNum(num)

# num = int(input())
# ans = pallindrome(num)
# print(ans)

#GCD
# def gcd(a,b):
#     divisor = min(a,b)
#     dividend = max(a,b)

#     while dividend%divisor != 0:
#         temp = dividend
#         dividend = divisor
#         divisor = temp%divisor
#     return divisor

# a = int(input())
# b = int(input())

# res = gcd(a,b)
# print(res)

#Armstrong
# def countDigits(num):
#     count = 0
#     while num > 0:
#         num = num//10
#         count += 1
#     return count
# def armstrong(num):
#     ans = 0
#     k = countDigits(num)
#     while num > 0:
#         rem = num%10
#         ans = ans + (rem**k)
#         num = num//10
#     return num == ans

# num = int(input())
# res = armstrong(num)
# print(res)

#Print All Divisor
# def allDivisors(num):
#     k = 1
#     while k*k <= 0:
#         if num%k == 0:
#             print(k)
#             if k !=(num//k):
#                 print(num//k)
#         k += 1

# num = int(input())
# res = allDivisors(num)
# print(res)

#Check for Prime
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




