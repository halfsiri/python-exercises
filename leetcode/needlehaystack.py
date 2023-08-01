class Solution(object):
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

test = Solution()
haystack = "sadbutsad"
needle = "but"
test2 = test.strStr(haystack,needle)
print(test2)
