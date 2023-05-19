import random

x = 1000000
randomList = list()

print(f"x={x}")

for i in range(x):
    element = random.randint(-1000, 1000)
    randomList.append(element)

randomList.sort()
print(randomList)
# підрахунок суми елементів списку за допомогою циклу for
sum_using_for = 0
for num in randomList:
    sum_using_for += num

print("sum of list using for loop:", sum_using_for)

# перевірка рівності з використанням вбудованої функції sum
if sum(randomList) == sum_using_for:
    print("The sums are equal")
else:
    print("The sums are not equal")
