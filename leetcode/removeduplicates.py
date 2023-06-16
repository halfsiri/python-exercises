"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        for num in nums:
            if num not in temp:
                temp.append(num)

        return temp


test = Solution()
nums = [1, 1, 2, 4, 6, 8, 8, 11]
result = test.removeDuplicates(nums)
print(result)


test = Solution()
nums = [1, 1, 2, 4, 6, 8, 8, 11]
result = test.removeDuplicates(nums)
print(len(result))
