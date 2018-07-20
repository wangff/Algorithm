# Dynamic Programming

## Two input, 2D array, Bottom-up

### 712. Minimum ASCII delete sum for two strings

##  From Recursive To Dynamic Prograimming

### 486. Predict the Winner

Reference: https://leetcode.com/problems/predict-the-winner/solution/

#### Approach #1 Using Recursion

1. The two players Play 1 and Play 2 will be taking turns alternately. For the Player 1 to be the winner, we need $score_{Player_1} \geq score_{Player_2}$. Or in other terms, $score_{Player_1} - score_{Player_2} \geq 0$.
2. Thus, for the turn of Player 1, we can add its score obtained to the total score and for Player2's turn, we can subtract its score from the total score. At the end, we can check if the total score is greater than or equal to zero, to predict that Player 1 will be the winner.
3. The value returned at every step is given by $turn*max(turn*a,turn*b)$. This is equivalent to the statement $max(a,b)$ for Player 1's turn and $ min(a,b) $ for Players2's turn. 
4. Time Complexity: $ O(2^n) $. Size of recursion tree will be $ 2^n $. Here, n refers to the length of nums array.
   Space complexity: $O(n)$. The depth of the recusion tree can go upto n.
   
#### Approach #2 Using Recursion with memory space

1. We can omit the use of turn to keep a track of the players for the current turn. If the current turn belongs to Player 1, we pick up an element, say x, from either end, and give the turn to Player 2. Thus, if we obtain the score for the remaining elements(leaving x), this score, now belongs to Player 2. Thus, since Player 2 is competing against Player 1, this score should be subtracted from Player 1's current score(x) to obtain the effective of Player 1 at the current instant.
2. In order to remove the duplicate function calls, we can make use of a 2-D memorization array, memo, such that we can store the result obtained for the function call winner for a subarray with starting and ending indices being se and e at memo[s][e]. This helps to prune the search space to a great extent.
3. Time complexity: $ O(n^2) $. The entire memo array of size nxn is filled only once. Here, n refers to the size of nums array.
   Space complexity: $ O(n^2) $. memo array of size nxn is used for memorization.

#### Approach #3 Dynamic Programming With 2-D Memory

1. D[s][e] donates the maximum score for the subarray nums[s][e]. The dp update equation is as follows:

    $$ dp[s][e] = max(dp[s]-dp[s+1][e], dp[s]-dp[s][e-1])$$
    
2. Based on the equation above, we can conclude s should range from down to up, and e should range from left to range.

3. dp[len(nums)-1][dp(nums)-1]=0

4. The start point should be from dp[len(nums)-2][len(nums)-1]

5. Time Complexity $O(n^2)$; Space complexity $ O(n^2)$


#### Approach #4 Dynamic Programming With 1-D Memory

1. From the DP equation: $ dp[s][e] = max(dp[s]-dp[s+1][e], dp[s]-dp[s][e-1])$, we could conclude that filling in any entry dp array, only elements in the next row(same column) and the previous column(same row) are needed


## To Be Selected Or Not To Be Selected

### 198. House Robbed

### 740. Delete And Earn 



