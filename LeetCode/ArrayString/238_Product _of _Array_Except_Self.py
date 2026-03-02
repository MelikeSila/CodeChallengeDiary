class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        all_products = 1

        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            if zero_count >= 2:
                break

        # if there are more than 1 zero than all answers will be zero
        if zero_count >= 2:
            return [0]*len(nums)
        # if there is just one zero than all answers will be zero except one nums[i]=0
        elif zero_count == 1:
            for j in range(0, len(nums)):
                if nums[j] != 0:
                    all_products *= nums[j]
                else:
                    index = j
            answer[index] = all_products
            return answer

        # O(n/2)
        n = len(nums)
        odd = 0
        if n%2 == 0:
            a = int(n/2)
        else:
            a = int(n/2) + 1
            odd = 1
        
        for i in range(0, a):
            all_products = all_products * nums[i] * nums[-i-1]
        
        if odd:
            all_products = all_products/nums[a-1]

        for i in range(0, a):
            answer[i] = int(all_products/nums[i])
            answer[-i-1] = int(all_products / nums [-i-1])
        
        
        return answer