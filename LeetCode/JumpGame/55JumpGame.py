class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
            
        if nums[0] <= 0:
            return False
        
        i =  0
        remained_max_step = nums[i]
        
        while len(nums)-1 > i:
            remained_max_step = max(remained_max_step, nums[i])
            
            if remained_max_step <= 0:
                return False

            i += 1
            remained_max_step -= 1

        return True