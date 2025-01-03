class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_tank = 0;
        int current_tank = 0;
        int start_index = 0;

        for(int i=0;i<gas.length;i++){
            int netGas = gas[i] - cost[i];
            total_tank += netGas;
            current_tank += netGas;

            if(current_tank < 0){
                start_index = i+1;
                current_tank = 0;
            }
        }

        if(total_tank < 0)
            return -1;
        else
            return start_index;   
    }
}

// Question: https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
