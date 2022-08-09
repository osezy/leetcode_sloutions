

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:  # looping through each word in the list of words
            count = [0] * 26

            for c in s:  # looping through each letter in word in the list
                count[ord(c) - ord('a')] += 1  # mapping the charters to index 0 to 25
                # and counting each charters in each word
            res[tuple(count)].append(s)

        return res.values()


solu = Solution()
word = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solu.groupAnagrams(word))
