#Hashing
#HashSet => Dictionary

#Count te frequency of each element in the array
arr = [1, 2, 1, 5, 3, 2, 7, 8, 1, 7, 10, 3, 8, 10]
print("Array: " + str(arr))

print()

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
print(d)

keyVal = d.items() #It provides a sequence with tuples in the format of (key, val)
print(keyVal)

#Max and Min count
mxCount = 0
mxVal = -1

mnCount = 1000000
mnVal = None

for (key, count) in d.items():
    if mnCount > count:
        mnVal = key
        mnCount = count

    if mxCount < count:
        mxVal = key
        mxCount = count

print(mnVal, mnCount)
print(mxVal, mxCount)