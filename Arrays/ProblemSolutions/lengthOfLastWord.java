class Solution {
    public int lengthOfLastWord(String s) {
        // Trim the whitespace at the end
        String trimmed = s.trim();
        int res=0;
        for(int i=trimmed.length()-1;i>=0;i--){
            if(trimmed.charAt(i) != ' ')  res+=1;
            else break;
        }
    return res;
    }
}

// Question: https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
