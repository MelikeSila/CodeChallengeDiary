import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = 0
        is_all_negative_flag = 1
        max_num_in_negative = -math.inf

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            current_sum += num

            if current_sum >= max_sum:
                max_sum = current_sum
                is_all_negative_flag = 0

            
            if current_sum < 0:
                current_sum = 0
                if max_num_in_negative < num:
                    max_num_in_negative = num
        
        if is_all_negative_flag:
            return max_num_in_negative

        return max_sum
        