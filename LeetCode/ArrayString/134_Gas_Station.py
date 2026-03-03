class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        sum_cost = 0
        sum_gas = 0
        for i in range(len(cost)):
            sum_cost += cost[i]
            sum_gas += gas[i]

        if sum_gas < sum_cost:
            return -1

        tank = 0
        start_station = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank < cost[i]:
                tank = 0
                start_station = i+1
            else: 
                tank -= cost[i]
        
        return start_station