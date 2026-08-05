class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = []
        for num in nums:
            if num not in k:
                k.append(num)
            else:
                k.pop()
        if len(k) == len(nums):
            return False
        return True

        