#!/bin/python3
# DONE
# 17.04.2024

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        m --> nums1 --> i
        n --> nums2 --> j
        """

        # lets fill from the back than we won't need an additional array
        i = m - 1
        j = n - 1
        e = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[e] = nums1[i]
                i -= 1
            else:
                nums1[e] = nums2[j]
                j -= 1
            e = e - 1

        # we are running on nums1 so checking only nums2 is enough for filling remaining part
        while j >= 0:
            nums1[e] = nums2[j]
            j -= 1
            e = e - 1
        
        

        

