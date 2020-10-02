class Solution:
    def __init__(self):
        self.combs = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.combs
        
    def dfs(self, nums, target, begin, comb):
        if target == 0:
            self.combs.append(comb)
            return
        if target < 0:
            return
        for i in range(begin, len(nums)):
            self.dfs(nums, target - nums[i], i, comb + [nums[i]])