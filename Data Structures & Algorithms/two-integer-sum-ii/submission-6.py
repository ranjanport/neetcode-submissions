class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left = 0
        # total = len(numbers)
        # for i in range(total):
        #     j = i + 1
        #     while j < total:
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1, j+1]
        #         j+=1

        # Hashmap
        maps = {}
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in maps:
                return [maps[k]+1, i+1]

            maps[numbers[i]] = i