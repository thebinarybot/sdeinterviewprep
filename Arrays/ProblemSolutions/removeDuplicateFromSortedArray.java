class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 1)
            return nums.length;
        
        int seen = 0;
        int next = 1;

        for(int i=1;i<nums.length;i++){
            if(nums[i] > nums[seen]){
                nums[next] = nums[i];
                next++;
                seen++;
            }
        }
    return next;
    }
}

// Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
