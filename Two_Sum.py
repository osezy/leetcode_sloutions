# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.

# TWO SUM
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # Creating a hash map
        perMap = {}

        # looping though the list
        for index, elem in enumerate(nums):

            # adding the diff btw the target and each element in the list to the hashmap
            comp = target - elem
            if comp in perMap:
                # returning the index of the number if already in the hash map
                return [perMap[comp], index]
            perMap[elem] = index
        # return an empty list if no element in the list gives the target
        return []


solu = Solution()
num = [1, 2, 5, 3, 2, 1, 4]
num1 = [8, 4, 2,  5, 7, 1]
num2 = [6, 2, 3, 1]
tag = 7
tag1 = 9
tag2 = 10
print(solu.two_sum(num, tag))
print(solu.two_sum(num1, tag1))
print(solu.two_sum(num2, tag2))