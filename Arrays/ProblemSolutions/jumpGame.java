import java.util.*;

class Solution {
    public boolean canJump(int[] nums) {
        int lastIndex = nums.length-1;
        for(int i=nums.length-1; i>=0; i--){
            if(i+nums[i] >= lastIndex)
                lastIndex = i;
        }
        return lastIndex == 0;
    }
}

// Question: https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
