class Solution {
    public int removeElement(int[] nums, int val) {
        int slow = 0; 
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        return slow;
    }
}

// Question: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
