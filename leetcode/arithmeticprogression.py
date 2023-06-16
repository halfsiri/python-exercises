"""

class Solution(object):

    def __init__(self):
        try:
            my_list = []
        
            while True:
                my_list.append(int(input()))
                self.list = my_list
            # if the input is not-integer, just print the list
        except:
            print(my_list)

    
    
    
    def canMakeArithmeticProgression(self):
        
        :type arr: List[int]
        :rtype: bool
        
        arr = sorted(self.list)
        print(arr)
        mde = self.mode(arr)
        el = self.DuplicatesCheck(arr)
        
        if len(arr) == 2:
            return True

        elif len(arr) > 1 and (mde != arr[1] or mde != arr[-2]):
            #while len(arr) > 1:
                
                    print((arr[0]) - (arr[1]))
                    print((arr[-2]) - (arr[-1]))
                    if (arr[0]) - (arr[1]) != (arr[-2]) - (arr[-1]) and abs(arr[0]) - abs(arr[1]) != abs(arr[-2]) - abs(arr[-1]): 
                        #print(arr[i])
                        #print(arr[0]) 
                        #print(arr[-1]) 
                        #print(arr[-2])
                        
                        return False
                    else:
                        #print(arr[i])
                        #print(arr[0]) 
                        #print(arr[-1]) 
                        #print(arr[-2])  
                        return True
        else:
            return False

    def DuplicatesCheck(self,arr):   
        for el in input_array:
            if input_array.count(el) > 1:
                return True
        return False
    

    def mode(self,arr):
     
    # creating a dictionary
        freq = {}
        for i in arr:
        
            # mapping each value of list to a
            # dictionary
            freq.setdefault(i, 0)
            freq[i] += 1
            
        # finding maximum value of dictionary
        hf = max(freq.values())
        
        # creating an empty list
        hflst = []
        
        # using for loop we are checking for most
        # repeated value
        for i, j in freq.items():
            if j == hf:
                hflst.append(i)
                
        # returning the result
        return hflst

#[-68,-96,-12,-40,16]
#[1,10,10,10,19]
list = Solution()

print(list.canMakeArithmeticProgression())
"""

class Solution(object):
    def __init__(self):
        try:
            my_list = []
        
            while True:
                my_list.append(int(input()))
                self.list = my_list
            # if the input is not an integer, just print the list
        except:
            print(my_list)

    def canMakeArithmeticProgression(self):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(self.list)
        diff = arr[1] - arr[0]  # Calculate the common difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

list = Solution()
print(list.canMakeArithmeticProgression())