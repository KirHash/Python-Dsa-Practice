#Reverse an array

# lst = [1, 2, 3, 4, 5]
# lst.reverse()
# print(lst)

# lst = list(map(int,input().split()))
# n = len(lst)
# for i in range(n//2):
#         lst[i], lst[n-1-i] = lst[n-1-i], lst[i]    
# print(lst)

# lst = list(map(int, input().split()))
# n = len(lst)

# a = 0
# b = n-1
# #2 pointer approach
# while a < b:
#     lst[a], lst[b] = lst[b], lst[a]
#     a += 1
#     b -= 1
# print(lst)

#2 pointer approach in recursion
lst = list(map(int, input().split()))
n = len(lst)
s = 0
e = n-1
def rev(s, e, lst):
    if s > e:
        return
    lst[s], lst[e] = lst[e], lst[s]
    rev(s+1, e-1, lst)
rev(s, e, lst)
print(lst)

