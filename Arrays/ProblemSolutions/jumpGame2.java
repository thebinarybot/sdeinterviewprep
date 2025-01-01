class Solution {
    public int jump(int[] nums) {
        if(nums.length == 1)
            return 0;
        
        int jumps = 0;
        int current_index = 0;
        int farthest = 0;

        for(int i=0; i<nums.length; i++){
            farthest = Math.max(farthest, i + nums[i]);
            if(i == current_index){
                jumps+=1;
                current_index = farthest;

                if (current_index >= nums.length-1)
                    break;
            }
        }

        return jumps;
    }
}

// Question: https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
