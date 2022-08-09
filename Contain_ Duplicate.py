# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        permap = set()

        # looping though the list
        for i in nums:
            # checking if the number is already in the set
            if i in permap:
                return True
            # adding the number to the set
            permap.add(i)
        return False


solu = Solution()
num = [1, 2, 3, 4]
result = solu.containsDuplicate(num)
print(result)