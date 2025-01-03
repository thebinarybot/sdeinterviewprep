class Solution {
    public int romanToInt(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == 'I') {
                total += 1;
            } else if (currentChar == 'V') {
                total += 5;
                if (i > 0 && s.charAt(i - 1) == 'I') {
                    total -= 2; // Subtract 2 for the previous 'I' 
                }
            } else if (currentChar == 'X') {
                total += 10;
                if (i > 0 && s.charAt(i - 1) == 'I') {
                    total -= 2; // Subtract 2 for the previous 'I' 
                }
            } else if (currentChar == 'L') {
                total += 50;
                if (i > 0 && s.charAt(i - 1) == 'X') {
                    total -= 20; // Subtract 20 for the previous 'X' 
                }
            } else if (currentChar == 'C') {
                total += 100;
                if (i > 0 && s.charAt(i - 1) == 'X') {
                    total -= 20; // Subtract 20 for the previous 'X' 
                }
            } else if (currentChar == 'D') {
                total += 500;
                if (i > 0 && s.charAt(i - 1) == 'C') {
                    total -= 200; // Subtract 200 for the previous 'C' 
                }
            } else if (currentChar == 'M') {
                total += 1000;
                if (i > 0 && s.charAt(i - 1) == 'C') {
                    total -= 200; // Subtract 200 for the previous 'C' 
                }
            }
        }
        return total;
    }
}

// Question: https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
