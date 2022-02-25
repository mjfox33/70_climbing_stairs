class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n < 3:
            return n
        previous = 2
        previous_previous = 1
        for _ in range(3,n+1):
            previous, previous_previous = previous + previous_previous, previous
        return previous