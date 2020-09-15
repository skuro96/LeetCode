class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        
        ans = 0
        place = 1
        while x >= place:
            ans *= 10
            ans += int(int(x % (place * 10)) / place)
            place *= 10

        if ans * sign < -2**31 or 2**31 - 1 < ans * sign:
            return 0

        return ans * sign