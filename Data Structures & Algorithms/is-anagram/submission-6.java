class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapS = new HashMap<>();
        for(char i: s.toCharArray()) {
           mapS.put(i, mapS.getOrDefault(i, 0)+1);
        }

        HashMap<Character, Integer> mapT = new HashMap<>();
        for(char i: t.toCharArray()) {
            mapS.put(i, mapS.getOrDefault(i, 0)-1);
        }

        for(HashMap.Entry<Character, Integer> entry: mapS.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            if(value != 0) {
                return false;
            }
        }
        return true;
    }
}
