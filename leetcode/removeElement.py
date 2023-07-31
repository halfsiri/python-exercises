
#import numpy as np
class Solution(object):

    """
    def __init__(self):
        self.nums = input("Nums: ")
        self.val = input("Val: ")
    """
        
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        #nums[:] = [x for x in nums if x != val]
        
        temp = []
        for num in nums:
            if val == num:
                continue
            else:
                temp.append(num)

        nums = [int(x) for x in temp]
        k = len(nums)
        # Assuming you want to return an integer array
        return nums
        #temp = np.array(nums)
        


test = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 0
result = test.removeElement(nums,val)
print(result)