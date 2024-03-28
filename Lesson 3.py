# Operations on Data Types

#String
firstName = "Kir"
lastName = "Hash"
name = firstName + " " + lastName
print(name)

#List
lst = [1,2,3,5,6,7,8]
lst.append(9)
print(lst)
lst.insert(3,4)
print(lst)
lst.pop(-1)
lst.pop(0)
print(lst)

#Tuple
tup = () #Representation
num = (3,4,5,6,7)
print(num[0])
print(num[-1])

#Dictionary
d = {} #Representation
prop = {
    "orange" : 5,
    "apple" : 7,
    "mango" : 4,
    "pulm" : 10
}
print(prop["orange"])
print(prop.get("pulm", -1))
prop["guava"] = 17
prop["banana"] = 22
print(prop)
del prop["banana"]
print(prop)

#Set
st = set() #Representation
st1 = {2,3,4,5,6,7,8}
print(st1, type(st1))
st1.add(13)
st1.add(7)
print(st1)
print(13 in st1)
print(20 in st1)
st1.remove(8)
print(st1)
