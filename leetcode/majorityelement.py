from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = []
        for i in nums:
            if i not in temp:
                print(test)
                temp.append(i)
            else:
                continue
        """
        for i in temp:
            if i in nums:
                nums.pop()
        """
        
        for i in temp:
            if nums.count(i)>len(nums)/2:
                n=i
            else:
                continue

        return n


        
        



test = Solution()
nums = [2,2,1,1,1,2,2]

test2 = test.majorityElement(nums)

print(test2)
