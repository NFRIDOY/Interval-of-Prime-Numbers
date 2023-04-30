const arr = [2, 4, 6, 8, 10]; // example array
const result = []; // to store the differences

for (let i = 0; i < arr.length - 1; i++) {
  const diff = arr[i+1] - arr[i]; // calculate the difference
  result.push(diff); // add the difference to the result array
}

console.log(result); // output: [2, 2, 2, 2]
