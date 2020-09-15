class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zig = [''] * numRows
        i = 0
        for k in range(len(s)):
            if k % (2 * numRows - 2) < numRows - 1:
                zig[i] += s[k]
                i += 1
            else:
                zig[i] += s[k]
                i -= 1
                
        return ''.join(zig)