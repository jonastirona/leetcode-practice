# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.
# logic: prefix product. iterate through array, keeping track of the product of all previous elements at each point in array. then go backwards in array, keeping track of postfix product. then for each element multiply prefix times postfix

class Solution:
    def productExceptSelf(self, nums):
        result = [1]*len(nums)

        prefix = 1

        for i, num in enumerate(nums):
            result[i] = prefix
            prefix*=num

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i]*=postfix
            postfix*=nums[i]

        return result