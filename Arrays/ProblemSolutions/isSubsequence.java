import java.util.*;

class Solution {
    public boolean isSubsequence(String s, String t) {
        int s1 = 0;
        int s2 = 0;
        while(s1 != s.length() && s2 != t.length()){
            if(s.charAt(s1) == t.charAt(s2)){
                s1++;
                s2++;
            }
            else{
                s2++;
            }
        }
        if(s1 == s.length())
            return true;
        else
            return false;
    }
}

// Question: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
