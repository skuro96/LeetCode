def isIn(c, dict):
    for i in dict:
        if c == i:
            return True
    return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        
        for i in range(len(s)):
            dict = []
            l = 0
            
            for j in range(i, len(s)):
                if isIn(s[j], dict) == False:
                    dict.append(s[j])
                    l += 1
                    if maxlen < l:
                        maxlen = l
                else:
                    break

        return maxlen