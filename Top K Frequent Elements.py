# Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from typing import List

# the count of each value in the input array is
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # hash map to count the occurrence  of each value
        freq = [[] for i in range(len(nums) + 1)]  # array to keep the count of value from the input array

        for n in nums:  # adding the occurrence of value into the count map
            count[n] = 1 + count.get(n, 0)  # if the count value is not in the map we put a default index of 0
        for n, c in count.items():  # lopping though and appending the count of each value
            freq[c].append(n)

        res = []  # creating the result list
        for i in range(len(freq)-1, 0, -1):  # lopping form the end of the array to the start
            for n in freq[i]:  # appending the of the count index to the result list
                res.append(n)
                if len(res) == k: # if res is equal k
                    return res


