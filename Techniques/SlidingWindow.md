# Sliding Window Technique
This Technique can be used to convert any nested loop problem into a single loop to reduce complexity.
Consider an array: [5,2,-1,0,3] and value of k = 3 and n = 5

Applying Sliding Window Technique:
1. Compute the sum of first k elements out of n terms using a linear loop and store the sum in variable window_sum.
2. Graze linearly over the array till it reaches the end and simultaneously keep track of maximum sum.
3. Get the current sum of block of k elements just subtract the first element from the previous block and add the last element of the current block .

Representation:
[5,2,-1,0,3]
Elements in Window: 5,2,-1
window_sum = 6

Now slide window by 1 element by using 
`window_sum = window_sum - arr[i] + a[i+k]`

Time Complexity is O(n).