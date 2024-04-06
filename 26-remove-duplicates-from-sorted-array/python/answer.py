class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i, x in enumerate(sorted(set(nums))): nums[i] = x
        sets = sorted(list(set(nums)))
        for i in range(len(sets)):
            nums[i] = sets[i]
        nums = nums[:len(sets)]
        return len(nums)
