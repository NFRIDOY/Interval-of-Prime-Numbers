arr = [2, 3, 5, 2, 8, 2, 9, 2]  # example array
count = 0  # to store the count of 2's

for num in arr:
    if num == 2:
        count += 1

print(count)  # output: 4

# With Function
def count_number(arr, num):
    count = 0
    for n in arr:
        if n == num:
            count += 1
    return count

arr = [2, 3, 5, 2, 8, 2, 9, 2]  # example array
num = 2  # example number to count
print(count_number(arr, num))  # output: 4
