from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        sorted_cards = sorted(freq.keys())

        for card in sorted_cards:
            while freq[card] > 0:
                for i in range(groupSize):
                    if freq[card+i] == 0:
                        return False
                    freq[card+i] -= 1
        
        return True

# Question: https://leetcode.com/problems/hand-of-straights/