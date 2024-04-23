#Palindrome or not

#In built function approach
# str = input()
# rev = reversed(str)

# if list(str) == list(rev):
#     print(True)
# else:
#     print(False)

#While Loop approach
# def isPal(s, e, str):
#     while s < e:
#         if n < 1:
#             return True
#         if str[s] != str[e]:
#             return False
#         s += 1
#         e -= 1
#     return True

# str = input()
# n = len(str)
# s = 0
# e = n-1

# res = isPal(s, e, str)
# print(res)

#For Loop approach
# def isPal(str):
#     for i in range(0, n//2):
#         if str[i] != str[-(i+1)]:
#             return False
#     return True

# str = input()
# n = len(str)

# res = isPal(str)
# print(res)


#Recursive approach
str = input()
n = len(str)

def isPal(s, e, str):
    if s > e:
        return True
    if str[s] != str[e]:
        return False
    return isPal(s+1, e-1, str)

res = isPal(0, n-1, str)
print(res)
