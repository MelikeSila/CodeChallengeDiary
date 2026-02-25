class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        i =  0
        n = len(nums)
        jump_count = 0
        remained_min_step = 0
        remained_max_step = nums[i]
        
        while n-1 > i:

            if nums[i] >= n-i-1:
                return jump_count + 1

            if nums[i] >= remained_max_step:

                remained_max_step = nums[i]
            
            if remained_min_step <= 0:
                jump_count += 1
                remained_min_step = remained_max_step


            i += 1
            remained_max_step -= 1
            remained_min_step -= 1

        return jump_count
