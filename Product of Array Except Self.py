# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # creating a result list of 1 making it equal to the len of the input array

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # the number at the index array result [res] now equal to new prefix
            prefix *= nums[i]  # prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):  # revering the loop
            res[i] *= postfix  # multiplying the res list by the new postfix
            postfix *= nums[i]  # postfix = postfix * nums[i]

        return res


solu = Solution()
num = [1, 2, 3, 4]
print(solu.productExceptSelf(num))



