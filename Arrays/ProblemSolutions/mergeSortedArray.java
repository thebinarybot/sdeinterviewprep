import java.util.*;
import java.io.*;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j = 0;
        for(int i=m; i<m+n; i++){
            nums1[i] = nums2[j];
            j++;
        }
        Arrays.sort(nums1);
    }
}

// Link To Question: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
