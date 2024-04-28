class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
            
        prev = nums[0]
        current_string = str(prev)
        new_array = []

        for i in range(1, len(nums)):
            if prev + 1 == nums[i]:
                prev = nums[i]
            else:
                if current_string != str(prev):
                    current_string += "->" + str(prev)
                
                
                new_array.append(current_string)
                current_string = str(nums[i])

            prev = nums[i]
        
        if current_string != str(prev):
            current_string += "->" + str(prev)
        new_array.append(current_string)
        return new_array
                


