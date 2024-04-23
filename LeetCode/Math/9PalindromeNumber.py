class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        x = str(x)
        size = len(x)//2

        for i in range(size):
            if x[i] != x[- i -1]:
                return False
        
        return True