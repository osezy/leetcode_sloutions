# Winning Card
# In a card game, each player will be given a set of random cards.
# Players will throw on the table their one winning card, the player with the highest card wins.
#
# A winning card is the card that only exists once in the set of cards, and the highest one.
#
# Given an array of sets of integers cards, return the card of the winning player. Return -1 If no such card is found.
#
# Example 1:
# Input: cards = [[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]
# Output: 8
#
# Example 2:
# Input: cards = [[5,5], [2,2]]
# Output: -1
#
# Constraints:
#
# 1 <= cards.length <= 2000
# 0 <= cards[i] <= 1000


def solution(cards) -> int:
    new = []
    res = -1
    for sub_card in cards:
        for card in sub_card:
            if card in new:
                new.remove(card)
            else:
                new.append(card)
    if len(new) == 0:
        return res
    highest = 0
    for i in new:
        if i > highest:
            highest = i
    return highest


num = [[5, 7, 3, 9, 4, 9, 8, 3, 1], [1, 2, 2, 4, 4, 1], [1, 2, 3]]
print(solution(num))


