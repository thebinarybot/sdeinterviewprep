class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        
        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();
        for(char c: s.toCharArray()){
            smap.put(c, smap.getOrDefault(c, 0)+1);
        }
        for(char c: t.toCharArray()){
            tmap.put(c, tmap.getOrDefault(c, 0)+1);
        }

        for(Map.Entry<Character, Integer> entry: smap.entrySet()){
            Character key = entry.getKey();
            Integer value = entry.getValue();

            if(!tmap.containsKey(key) || !tmap.get(key).equals(value))
                return false;
        }
        return true;
    }
}

// Question: https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
