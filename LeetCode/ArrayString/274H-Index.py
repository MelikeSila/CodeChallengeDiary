class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # how many papers has the i and more citations = control_array[i]
        n = len(citations) + 1
        control_array = [0]*n
        
        for c in citations:
            if c > n - 1:
                control_array[n-1] += 1
            else:
                control_array[c] += 1

        i = n - 1

        cumulative_citations = 0
        while i >= 0:
            if control_array[i] + cumulative_citations >= i:
                return i
            
            cumulative_citations += control_array[i]
            i -= 1

        return 0