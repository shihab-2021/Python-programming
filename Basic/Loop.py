# While loop start
num = 1
sum = 0
while num <= 10:
    sum = sum + num
    num = num + 1
print(sum)
i=1
while(i<10):
    print(i,end=" ")
    i+=1
    if i==5:
        break
print("\n")
# While loop end

# for loop start
country = 'Bangladesh'
for letter in country:
    print(letter)

for num in range(5):
    print(num)

for index in range(6, 13):
    print(index)

for n in range(5, 45, 5):
    print(n)

a="Bd"
for i in range(len(a)):
    print(a[i],end="")

# reverse print
for i in range(39, 13, -2):
    print(i)
# for loop end