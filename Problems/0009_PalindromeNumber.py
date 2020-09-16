class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_cp = x
        rev = 0
        while x_cp >= 10:
            rev *= 10
            rev += x_cp % 10
            x_cp = int(x_cp / 10)
        rev = rev * 10 + x_cp
        
        if x == rev:
            return True
        else:
            return False