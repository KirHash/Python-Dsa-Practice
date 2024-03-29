# Loops

# name = "Kirhash"

# for i in range(101):
#     print(name + " " +str(i))

# pushup = 0

# while pushup <= 15:
#     print(str(pushup) + " pushup")
#     pushup += 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = -1
a = 100
for i in range(len(nums)):
    if nums[i] == a:
        ans = i
        break

print(ans)

    
    