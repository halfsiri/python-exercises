class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            nums.insert(nums.index(target),target)
            return nums.index(target)
        elif target == 0:
            k = nums[min(range(len(nums)), key = lambda i: abs(nums[i]-target))]
            if k > target:
                nums.insert(nums.index(k),target)
            else:
                nums.insert(nums.index(k+1),target)
            temp = nums.index(target)
            return temp

        elif target not in nums:
            k = nums[min(range(len(nums)), key = lambda i: abs(nums[i]-target))]
            print(k)
            if k > target:
                nums.insert(nums.index(k),target)
            else:
                nums.insert(nums.index(k+1),target)
            temp = nums.index(target)
            return temp
        else:
            return -1

test = Solution()
nums = [3,6,7,8,10]
target = 0
test2 = test.searchInsert(nums,target)
print(test2)
