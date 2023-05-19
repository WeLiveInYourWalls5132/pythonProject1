import random
a = []
for i in range(100):
    a.append(random.randint(0, 10000))

#==
#>=
#>
#<
min = 10000
for i in a:
    if i < min:
        min = i
print (min)
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
s