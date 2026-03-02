class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        all_product = 1
        import numpy as np

        zero_count = len(nums) - np.count_nonzero(nums)
        print(f"zero count: {zero_count}")

        # if there are more than 1 zero than all answers will be zero
        if zero_count >= 2:
            return [0]*len(nums)
        # if there is just one zero than all answers will be zero except one nums[i]=0
        elif zero_count == 1:
            for j in range(0, len(nums)):
                if nums[j] != 0:
                    all_product *= nums[j]
                else:
                    index = j
            answer[index] = all_product
            return answer


        all_products = 1
        for n in nums:
            all_products *= n
        
        for i in range(0, len(nums)):
            answer[i] = int(all_products / nums[i])
        
        
        return answer