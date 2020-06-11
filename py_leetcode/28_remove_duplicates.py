from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniquiElementCounter = 1
        
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        for id in range(1,len(nums)):
            if nums[id] != nums[id-1]:
                nums[uniquiElementCounter] = nums[id]
                uniquiElementCounter+=1
                
        return uniquiElementCounter