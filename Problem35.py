class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target < nums[l]:
            return l
        if target > nums[r]:
            return r + 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


test = [1,3,5,7]
print Solution().searchInsert(test, 0)