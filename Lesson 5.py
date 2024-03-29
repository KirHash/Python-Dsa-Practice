# Slicing in Python

name = "KirHash"
print(name[0:5:2]) # start:end:step
print(name[0:3])
print(name[-1::-1])

lst = [1, 2, 3, 4, 5, 6]
print(lst[-1::-1])
print(lst[-1:0:-1])

print(lst, id(lst))
lst.append(7)
print(lst, id(lst))

lst.append(8) # append(element)
print(lst)

lst.insert(0, 29) # insert(index, element)
print(lst)

lst.pop(0) # pop(index)
print(lst)

lst.remove(8) # remove(element)
print(lst)

statement = "I, am, a, Great, Teacher"
lst = statement.split(",")
print(lst)

color = ["Red", "Green", "Blue", "Black"]
res = "-".join(color)
print(res)
