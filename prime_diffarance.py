arr = [2, 3, 5, 7, 9]  # example array
result = [0]  # to store the differences

for i in range(len(arr)-1):
    diff = arr[i+1] - arr[i]  # calculate the difference
    result.append(diff)  # add the difference to the result array

print(result)  # output: [2, 2, 2, 2]
