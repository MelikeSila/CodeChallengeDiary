class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        markedWords = {}

        if len(s) != len(t):
            return False
        values = []
        markedWords[s[0]] = t[0]
        for i in range(1, len(s)):
            if (s[i-1] == s[i] and t[i-1] != t[i]) or (s[i-1] != s[i] and t[i-1] == t[i]):
                return False

            if s[i] in markedWords:
                if markedWords[s[i]] != t[i]:
                    return False
            else:
                if t[i] in values:
                    return False
                markedWords[s[i]] = t[i]
                values.append(t[i])
        
        return True
