class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k%n;

        reverse(nums, 0, n-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, n-1);

    }
    public void reverse(int[] nums, int start, int end){
        while(start < end){
            swap(nums, start, end);
            start++;
            end--;
        }
    }
     public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}

// Question: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150