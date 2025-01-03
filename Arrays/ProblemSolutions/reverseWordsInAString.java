import java.util.*;

class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder result = new StringBuilder();
        int left = 0;
        int right = words.length - 1;
        
        while(left<right){
            swap(words, left, right);
            left++;
            right--;
        }

        for(int i=0; i<words.length; i++){
            result.append(words[i]);
            result.append(" ");
        }

        return result.toString().trim();
    }
    public void swap(String[] words, int left, int right){
        String temp = words[left];
        words[left] = words[right];
        words[right] = temp;
    }
}

// Question: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
