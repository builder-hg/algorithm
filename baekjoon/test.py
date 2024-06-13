def isNStraightHand(hand, groupSize):
    """
    :type hand: List[int]
    :type groupSize: int
    :rtype: bool
    """
    if len(hand) % groupSize != 0:
        return False

    _dict = {}
    for i in range(len(hand)):
        now = hand[i]
        _dict[now] = _dict.get(now, 0) + 1

    idx = 0
    hand.sort()
    while idx < len(hand):
        now = hand[idx]

        if _dict[now] == 0:
            idx += 1
            continue
        
        _dict[now] -= 1

        for i in range(1, groupSize):
            nxt = now + i

            if nxt not in hand:
                return False
            
            if _dict[nxt] <= 0:
                return False
            
            _dict[nxt] -= 1

        idx += 1

    return True
    
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))