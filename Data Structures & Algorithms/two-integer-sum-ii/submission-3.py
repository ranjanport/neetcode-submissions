class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        total = len(numbers)
        for i in range(total):
            j = i + 1
            while j < total:
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
                j+=1