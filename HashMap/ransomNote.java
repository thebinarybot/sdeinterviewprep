import java.util.*;
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length())
            return false;
        
        HashMap<Character, Integer> count = new HashMap<>();

        for(char c: magazine.toCharArray()){
            count.put(c, count.getOrDefault(c,0)+1);
        }

        for(char c: ransomNote.toCharArray()){
            if(count.containsKey(c) && count.get(c)>0){
                count.put(c, count.get(c)-1);
            }
            else
                return false;
        }

        return true;
    }
}

// Question: https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
