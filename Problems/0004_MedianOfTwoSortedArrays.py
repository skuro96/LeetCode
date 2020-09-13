def marge(l1, l2):
    i = 0
    j = 0
    ans = []
    while i < len(l1) or j < len(l2):
        if j >= len(l2) or i < len(l1) and l1[i] < l2[j]:
            ans.append(l1[i])
            i += 1
        else:
            ans.append(l2[j])
            j += 1
    return ans

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = marge(nums1, nums2)
        n = len(array)
        if n % 2 == 1:
            return array[int((n - 1) / 2)]
        else:
            return (array[int(n / 2)] + array[int(n / 2 - 1)]) / 2