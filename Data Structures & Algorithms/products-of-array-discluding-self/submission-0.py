class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        final_list = [1]*length

        k = 1
        for i in range(length):
            final_list[i] = final_list[i] * k
            k *= nums[i]

        k  = 1
        for i in range(length-1, -1, -1):
            final_list[i] = final_list[i] * k
            k *= nums[i]
        return final_list