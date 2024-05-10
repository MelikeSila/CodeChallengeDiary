class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = -1

        while i != -len(digits)-1:
            
            if digits[i] == 9:
                if i == -len(digits):
                    digits[i] = 0
                    return [1] + digits
                else:
                    digits[i] = 0
            else:
                digits[i] += 1
                return digits

            i -= 1

        return digits