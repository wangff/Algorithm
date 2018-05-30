# PrefixSum Approach to solve SubPath Sum Problems

## intuition

sum[i] represents the sum from 0 index upto i^th index.
If the cumulative sum upto two indices is the same, the sum of the elements lying in between those indices is zero.
If the cumulative sum upto two indices, has a difference of k (sum[i]-sum[j] = k), the sum of elements lying between indices i and j is k.

Therefore, if there are count[sum[j]] kinds of ways to get sum[j], we would have count[sum[j]] different j as start position. Then we have count[sum[j]] different sub sequences from those start position, and the sum of those sequences is equal to k.

i.e
array: [1,2,-1,-1,2]; target=2
sum:   [1,3,2,1,3]

result 1: 
sum(1)-sum(0)=sum(array[1])=2
startPos = 0
sum(startPos)=1

result2:
sum(4)-sum(0) = sum(array[1],array[2],array[3],array[4]) =2 
startPos = 0
sum(startPos)=1

result3:
sum(4)-sum(3) = sum(array[4])=2
startPos = 3
sum(startPos)=1

Therefore, there are three subarrays which sum are equal to target

## Typical Problems

1.  [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/) Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
2.  [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/description/) You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

### Differences Between Two Problems

560 processes the array, the direction of going on is only one.
437 processes the binary tree, the direction of going on is two.








