class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] swords = s.split(" ");
        if(pattern.length() != swords.length)
            return false;

        HashMap<Character, String> follows = new HashMap<>();
        for(int i = 0; i < pattern.length(); i++) { 
            char c = pattern.charAt(i);
            if(follows.containsKey(c)) {
                if(!follows.get(c).equals(swords[i])) {
                    return false;
                }
            } else {
                if(follows.containsValue(swords[i])) {
                    return false;
                }
                follows.put(c, swords[i]);
            }
        }
        return true;
    }
}

// Question: https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
