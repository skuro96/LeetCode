def covered(a, b): # a is coverd with b
    return b[0] <= a[0] and a[1] <= b[1]

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        i = 0
        while i < n:
            for j in range(len(intervals)):
                if i == j:
                    continue
                if covered(intervals[i], intervals[j]):
                    intervals.pop(i)
                    i -= 1
                    n -= 1
                    break
            i += 1
        return len(intervals)