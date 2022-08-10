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


bot = input("bot").u