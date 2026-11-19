# Part 1 - Find Maximum and Sort List

arr = [8, 3, 15, 6, 2]

# Find maximum
maximum = arr[0]
comparisons = 0

for i in range(1, len(arr)):
    comparisons += 1
    if arr[i] > maximum:
        maximum = arr[i]

print("Input:", arr)
print("Maximum:", maximum)
print("Comparisons:", comparisons)

# Bubble Sort
sorted_arr = arr.copy()

for i in range(len(sorted_arr)):
    for j in range(len(sorted_arr)-1-i):
        if sorted_arr[j] > sorted_arr[j+1]:
            sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]

print("Sorted List:", sorted_arr)