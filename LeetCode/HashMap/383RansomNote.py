class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        allLetters = {}
        for m in magazine:
            if m in allLetters:
                allLetters[m] += 1
            else:
                allLetters[m] = 1
        
        print(allLetters)

        for r in ransomNote:
            if r in allLetters and allLetters[r] != 0:
                allLetters[r] -= 1
            else:
                return False
        
        return True