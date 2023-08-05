class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if " " in s:
            lastword = s[s.rindex(" "):].strip()
        else:
            lastword = s
        #lastword = lastword.strip()
        return lastword

test = Solution()
s = "a"
test2 = test.lengthOfLastWord(s)
print(test2)

