class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> SMap = new HashMap<Character, Integer>();
        Map<Character, Integer> TMap = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++) {
            SMap.put(s.charAt(i), SMap.getOrDefault(s.charAt(i), 0) + 1);
        }

        for(int i = 0; i < t.length(); i++) {
            TMap.put(t.charAt(i), TMap.getOrDefault(t.charAt(i), 0) + 1);
        }

        if(TMap.equals(SMap)){
            return true;
        }
        return false;
    }
}