class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = [str(i) for i in digits]
        temp2 = int("".join(temp))+1
        temp3 = str(temp2)
        temp4 = []
        for i in range(len(temp3)):
            temp4.append(int(temp3[i]))
        
        return temp4


test = Solution()
digits = [1,2,3]
test2 = test.plusOne(digits)
print(test2)