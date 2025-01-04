class Solution {
    public boolean isPalindrome(String s) {        
        // Convert all characters to lowercase
        s = s.toLowerCase();
        // Remove all non-alphanumeric characters
        s = s.replaceAll("[^a-zA-Z0-9]","");

        // Check if palindrome using 2 pointers
        int start = 0;
        int end = s.length()-1;

        while(start < end){
            if(s.charAt(start) != s.charAt(end))
                return false;
            start++;
            end--;
        }

        return true;
    }
}

// Question: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
