#Problem number 283 - Move Zeros
#class Solution(object):

def main():
    nums = 1, 2, 0, 4, 0, 5 
    self = 0
    moveZeroes(self, nums)

def moveZeroes(self, nums):

        l = 0
        #for current in nums:
        for r in range(len(nums)):
            if (nums[r] != 0): #finding non zero elements
                #temp = nums[following] 
                #nums[following] = nums[lead]
                #nums[lead] = temp
                nums[r], nums[l] = nums[l], nums[r] 
                #Setting right pointer to left = Setting left pointer to right
         
                l += 1 #increment left pointer
           
            








