class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        return len(set(nums)) < len(nums)