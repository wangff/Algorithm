## DP - Best Time to Buy and Sell Stock

### 121 Best Time to Buy and Sell Stock I

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

```python
for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit,price - minPrice)
```



### 122. Best Time to Buy and Sell Stock II

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

```python
while i < length-1:
            if(prices[i] < prices[i+1]):
                profit += prices[i+1] - prices[i]
            i += 1
```



### 123. Best Time to Buy and Sell Stock III

Design an algorithm to find the maximum profit. You may complete at most *two* transactions.

You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

### 188. Best Time to Buy and Sell Stock IV

Design an algorithm to find the maximum profit. You may complete at most **k** transactions.

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

### DP Solution

1. Subproblem
   1. DP[k,i] the max income for 0 to i elements at most k transactions.
2. Recurrence formular
   1. if we don't use element i
      1. dp[k,i] = dp[k,i-1]
   2. if we use element i
      1. dp[k,i] = max(prices[i] - prices[j] + dp[k-1,j]) for all j in [0,i-1] inclusive range
      2. dp[k,i] = pricces[i] - min(prices[j] + dp[k-1,j]) for all j in [0, i-1] inclusive range
      3. since min(prices[j] + dp[k-1,j]) would change dependent i, we could merge the for all j loop to i loop
3. Initialization
   1. since when transaction is 0, no matter how many elements, the income is 0.
   2. when there are only 1 element, cannot construct trasaction, so the result is also