# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import List


class Sloution:
    def reversenumber(self, head: List[int] ) -> List[int]:
        perv, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = perv
            perv = curr
            curr = nxt
        return perv


solu = Sloution()
num = [1,2,34]
print(solu.reversenumber(num))
