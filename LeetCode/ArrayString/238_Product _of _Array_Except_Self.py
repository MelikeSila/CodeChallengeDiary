class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [a, b, c, d]
        # nums[i]*nums[i+1] = x --> i = 0
        # nums[j]*nums[j-1] = y --> j = len(nums)
        # x = [a, ab, abc, abcd] --> shift to right --> [1, a, ab, abc]
        # y = [abcd, bcd, cd, d] --> shift to left -->  [bcd, cd, d, 1]
        # multiply x and y --> [bcd, acd, abd, abc] --> our results

        results = [1]*len(nums)
        x = [1]*len(nums)
        y = [1]*len(nums)

        # calculate x
        cumulative = 1
        for i in range(len(nums)-1):
            x[i+1] = nums[i]*cumulative
            cumulative *= nums[i]
        
        # calculate y
        cumulative = 1
        for i in range(len(nums)-1, 0, -1 ):
            y[i-1] = nums[i]*cumulative
            cumulative *= nums[i]

        # x*y
        for i in range(len(results)):
            results[i] = x[i]*y[i]

        return results