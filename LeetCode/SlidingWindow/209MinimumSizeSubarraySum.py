class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        remove_index = 0
        total = 0
        output = 0
        min_output = 1000000000 # 10^9

        # return 1 if the target is in the nums
        if target in nums:
            return 1

        for n in nums:
            total += n
            output += 1
            
            # move the index at the beggingin and remove it from the slided part
            while total - nums[remove_index] >= target:
                total -= nums[remove_index]
                remove_index += 1 
                output -= 1
            
            # keep the length of minumum lenght sub array
            if total >= target:
                min_output = min(output, min_output)
                
        if total >= target:
            return min_output
        
        return 0
            