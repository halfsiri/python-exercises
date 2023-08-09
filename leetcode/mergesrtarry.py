from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        for i in nums2:
            nums1.append(i)
        nums1.sort()
        s = map(str, nums1)
        s = ''.join(s)
        s = int(s)
        print(s)
        s = str(s)
        nums1 = []
        print(nums1)
        nums1 = [int(x) for x in s]

       
        nums1 = [i for i in nums1 if i != 0]
        nums2 = [i for i in nums1 if i != 0]
        for i in nums2:
            nums1.append(i)
        
       
        nums1.sort()

        
        
        return nums1
         """
        nums1.sort()
        nums2.sort()
        nums1=nums1[len(nums1)-m:len(nums1)]
        nums2=nums2[len(nums2)-m:len(nums2)]

        for i in nums2:
            nums1.append(i)
        nums1.sort()
        
        print(nums1)
        



test = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

test2 = test.merge(nums1,m,nums2,n)