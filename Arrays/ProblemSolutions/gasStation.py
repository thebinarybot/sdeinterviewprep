class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        total = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if tank < 0:
                start = i+1
                tank = 0
        
        if total >= 0:
            return start
        else:
            return -1

# https://leetcode.com/problems/gas-station/