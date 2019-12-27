## Using stack to implement the monotonic increasing or descreasing array

### Monotonic stack

1. in stack, store the index.

2. Monotonic increasing queue: to push an element, we pop out element stacktop >= current pointer in the traverse

   1. the stack keeps increasing from the push in direction.
   2. after pop out, the stack[-1] is the next smaller and largest smaller in the push in direction.
   3. During while pop, each pop is larger than all elements in stack, and also large than current point
   4. During while pop, the first pop element is larger than the next pop elemts
   5. code

   ```pseudocode
   for start to end:
       while stack and A[stack[-1]] >= A[current pointer]:
           stack.pop()
       if stack:
           nextSmaller[i] = stack[-1]    
       stack.append(i)    
   ```

   1. However,  the current point is the next smaller of all the pop out from stack

   ```pseudocode
   from start to end:
   	while stack and A[stack[-1]] >= A[current pointer]:
   		nextSmaller[stack.pop()] = stack[-1]
   	nextSmaller[i] = -1
   	stack.append(i)
   ```

   

3. Monotonic decreasing queue: 

   1. the stack keeps decreasing from the push in direction.
   2. after pop out, the stack[-1] is the next larger and smallest larger element in the push in direction.
   3. During while pop, each pop is smaller than all elements in the stack, and also smaller than current
   4. During while loop, the first pop element is smaller than the next pop elements
   5. code

   ```pseudocode
   for start to end:
       while stack and A[stack[-1]] <= A[current pointer]:
           stack.pop()
       if stack:
           nextLarger[i] = stack[-1]    
       stack.append(i)    
   ```

   1. However,  the current point is the next smaller of all the pop out from stack

   ```
   from start to end:
   	while stack and A[stack[-1]] >= A[current pointer]:
   		nextLarger[stack.pop()] = stack[-1]
   	nextLarger[i] = -1
   	stack.append(i)
   ```

   

4. For regular monotonic stack (either in increasing or decreasing order) the top of stack is the next smaller or next larger in the push in direction.

   1. If we want the the next smallest or next largest ones.
   2. change the model.
   3. sorted the index by its value, saying in increasing order, saying B, and the original one is 
   4. so for current pointer in B, all of its right values in B have increasing larger values in A.
   5. so for the current pointer in B, find the next larger one in B. which is the smallest value in A than current one is A, and of course in the right direction.

5. LC739: Daily Temperatures

   1. for current, we want to know next warmer temperature, for current to the end,
   2. so from pushing in direction, we want first element larger than current element, we choose decreasing monotonic queue from the rear

6. LC581

   1. from the left, find the smallest index who violate the increasing order
      1. from the left, construct monotonic increasing order
   2. from the right, find the largest index who violate the descending order
      1. from the right, construct monotonic decreasing order 

7. LC496 Next Greater Element I

   1. from the push in direction, find the first greater
   2. from the right, build the descending monotonic stack
   3. the top of stack is the next greater of current position

8. LC 503 the same as regular one

   1. double range
   2. use % len to index

9. LC 84 Largest Rectangle in Histaogram

   1. for each element, find left bound, right bound
   2. left bound is first smaller element from the left direction
   3. right bound is first smaller element from the right direction
   4. the large area that the current histogram could form is (right-left-1)*height

10. LC 85

   1. tranverse row by row, for each row
      1. computer the heights for this row based the last row
      2. calculate the max Rectangle by using 84 algorithms

11. LC862

    1. Rephrase the problem:
       1. build the prefix sum array P
       2. opt(y), y is current visit, largest x so that x < y, and p[x]<= p[y]- k
    2. for y, find the first smaller element p[x], so that p[y]-p[x]>=k
    3. if exist z < x < y, but p[z] > p[x] and p[z] < p[y]. if p[z] is candidate, p[x] must be candidate and x > z, so x must bu the true candidate, so z must not be candidate.
    4. So the candidates should be increasing sequence before y.
    5. we could use increasing monotonic stack from left.
    6. And then reverse traverse to find the largest x so that, p[x]<= p[y]- k. this way would out time limit
    7. so alternatively, we choose from the left to traverse the stack, and popleft the elements that have been processed.
       1. since if exists some x, to make y1 meet the requirements, y2 (y2 > y1) will never be the better candidates. 
       2. so we should change the data structure from stack to dequeue

12. LC 907 Sum of Subarray Minimums = LC 84

    1. Every element in the original array has a chance to be min, 
    2. So for each element, we count the probability  that each element becomes the min
    3. there are two situation:
       1. this element as the right-most one, which is the min of the subarray
       2. this element as the left-most one, which is the min of the subarray
    4. The current visit element is the right-most min, say A[y]
       1. we should find the next smaller than current element from the left, say A[x]
       2. the probability thatA[y] is the smallest one, is number of subarray [i:y]; i in [x+1:y], which is y-x
    5. The current visit element is the left-most min,
       1. we should find the next smaller than current element from the left
    6. `return sum((i-left[i](*(right[i]-i)*A[i] for i in range(len(A))`

13. LC975 Odd Even Jump

    1. During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value. 
       1. for odd jumps, for current visit position i, find the next samllest larger element j
       2. construct new list B, elements in B is the index of A, and the order in B is the increasing order of A's values.
       3. so B is an index array. For any index in B, its right peers has larger values than its value in A.
       4. Also, its immediately right one is the smallest larger one.
       5. For array A, find the next one in the right direction.
       6. So, for array B, find the next larger one.
       7. For B, construct descending monotonic stack from the right.
       8. the stack top is the next larger one for current pointer.
    2. During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the largest such index j.
       1. for even jumps, for current visit position i find the next largest smaller element j
       2. Construct B, B is the index of A, and the order in B is the decreasing order of A' values
    3. Dynamic Programming
       1. for every point in the list A, there are two status: odd step or even step
       2. transfer formula: 
          1. `odd[i] = even[oddnext[i]] if oddnext[i] exists`
          2. `even[i] = odd[evennext[i]] if evennext[i] exists`
       3. Basic situation
          1. `odd[N-1] = True`
          2. `even[N-1] = True`
       4. the start point is the first step, so we just count odd list.

14. LC1130 Minimum Cost Tree From Leaf Values

Idea:

1. since each node has either 0 or 2 children, 

we have to combine two adjacent nodes until only one left in the array.

2. we have two choice to combine, left + mid, or mid + right

3. since we want to minimize the res, at each time res += max of left subtree * max of right subtree
4. so we choose the minmum side to combine.
5. Since every time when we combine, we just need the max leaf in each subtree, so we just keep the max leaf after combination

Solution:

1. we keep a monotonic decreasing array
2. when we meet a new leaf large than the last element, the last element would be a local valley. we will comibination the minimu ones, and keep the max leaf.