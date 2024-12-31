class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> occurances = new HashMap<>();
        for(int num: nums){
            occurances.put(num, occurances.getOrDefault(num,0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : occurances.entrySet()) {
            if (entry.getValue() > nums.length / 2) {
                return entry.getKey(); 
            }
        }
        return 0;   
    }
}

// Question: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
// To-Do: Solve with Boyer Moore Algorithm
