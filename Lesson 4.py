#Coversion between datatypes

a = 4.5 #float

a1 = int(a) 
print(a1, type(a1))

a2 = str(a)
print(a2, type(a2))

lst = [1,2,3,4,5]

lst1 = tuple(lst)
print(lst1, type(lst1))

lst2 = set(lst)
print(lst2, type(lst2))

color = ["red", "blue", "green"]
qty = [2, 4, 6]

lst3 = dict(zip(color, qty))
print(lst3, type(lst3))

print(bool([]), bool({}), bool(""), bool(0), bool(0.0))
print(bool([2]), bool({5: "Human"}), bool("Hello"), bool(3), bool(4.5))

a3 = (2) #Exception Case

#Note: Zip can only be converted into dict
