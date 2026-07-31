# Part 4 - Count the Steps

count = 0

for i in range(1, 6):
    print(i)
    count += 1

print("Single Loop Runs:", count)

count2 = 0

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count2 += 1

print("Nested Loop Prints:", count2)

n = 10

print("Single Loop for n=10:", n)
print("Nested Loop for n=10:", n * n)