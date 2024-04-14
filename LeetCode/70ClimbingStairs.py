'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
___________________
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps



Example 2:
___________________
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''


# It is kind of fibbonacci problem
# if n = 1 has 1 way and n = 2 has 2 vays
# then n = 1 + 2 = 3 has 1 way + 2 ways = 3 ways

#!/bin/python3
# DONE
# 12.04.2024

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)  # create an n size zero array. +1 for initial value
        
        dp[0] = 1   # initial value to reach 2 step
        dp[1] = 1   # for climb 1 step

        # find the combinations for n'th step.
        # there is 2 options to take step: 1, and 2
        # then to reach the step n we can sum the set of combinations: dp[n-1] and dp[n-2]
        # because if we know the set of combinations to take n-1 step we need to take 1 more step and reach to nth step.
        # so the number of set combination for n-1 is also the a part of the combinations for to take n steps stairs.
        # and same for n-2.
        # then dp[n] = dp[n-1] + dp[n-2]

        # If we had the third option that let us take 3 steps:
        # We would consider dp[n-3] because with taking 3 step we can reach n.
        # Thus the result would be dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]