import java.util.*;

class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        Arrays.sort(citations);

        int hIndex = 0;
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) { 
                hIndex = Math.max(hIndex, n - i); 
            }
        }

        return hIndex;
    }
}

// Question: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
