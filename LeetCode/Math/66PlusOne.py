class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = -1
        l = len(digits)

        while i != -l-1:
            
            if digits[i] == 9:
                digits[i] = 0
                if i == -l:
                    return [1] + digits
            else:
                digits[i] += 1
                return digits

            i -= 1

        return digits