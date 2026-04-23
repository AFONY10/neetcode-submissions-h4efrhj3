class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)

        
        nums1.sort()
        print(nums1)
        lp = 0
        rp = len(nums1) - 1
     
        mp = (rp+lp) // 2
        print(mp)
        if len(nums1) % 2 == 0:
            average = (nums1[mp] + nums1[mp+1])/2
            return average
        else:
            print(float(mp))
            return float(nums1[mp])
            

        return 0.0


        