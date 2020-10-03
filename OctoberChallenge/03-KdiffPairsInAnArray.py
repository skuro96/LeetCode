class Solution:  
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        cnt = 0
        
        if k == 0:
            counts = collections.Counter(nums)
            for key, val in counts.items():
                if val >= 2:
                    cnt += 1
            return cnt
        
        nums = set(nums)
        for num in nums:
            if num + k in nums:
                cnt += 1
        return cnt


""" Ver.1
def diff(k, pair):
    if pair[0] - pair[1] == k or pair[1] - pair[0] == k:
        return True
    else:
        False

def isSame(p1, p2):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return True
    elif p1[0] == p2[1] and p1[1] == p2[0]:
        return True
    else:
        return False

class Solution:
    def __init__(self):
        self.pairs = []
        
    def exist(self, a_pair):
        for p in self.pairs:
            if isSame(p, a_pair):
                return True
        return False
    
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = int(len(nums))
        for i in range(n):
            for j in range(i + 1, n):
                tmp = [nums[i], nums[j]]
                if diff(k, tmp) == True and self.exist(tmp) == False:
                    self.pairs.append(tmp)
        return len(self.pairs)
"""