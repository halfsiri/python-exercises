from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            try:
                n = nums.index(target)
                return n
            except:
                return(-1)

test = Solution()
nums = [-1,0,3,5,9,12]
target = 12

test2 = test.search(nums,target)
print(test2)