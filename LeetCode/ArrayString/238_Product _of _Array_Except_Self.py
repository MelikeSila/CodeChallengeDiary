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



        answer_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in answer_dict:
                answer[i] = answer_dict[nums[i]]
            elif nums[i]*-1 in answer_dict:
                answer[i] = answer_dict[nums[i]*-1] * -1
                answer_dict[nums[i]] = answer_dict[nums[i]*-1] * -1
            else:
                all_product = 1
                for j in range(0,len(nums)):
                    if j != i:
                        all_product *= nums[j]
                answer[i] = all_product
                answer_dict[nums[i]] = answer[i]
        
        
        return answer