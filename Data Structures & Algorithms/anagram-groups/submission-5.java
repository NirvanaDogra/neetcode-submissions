
class Solution {
    public String isAnagram(String str) {
        int[] count = new int[26];
        for (char s : str.toCharArray()) {
            count[s - 'a']++;
        }
        
        // Using StringBuilder is much more efficient than String concatenation
        StringBuilder sb = new StringBuilder();
        for (int i : count) {
            sb.append('#').append(i); // '#' helps distinguish counts (e.g., '1' and '11')
        }
        return sb.toString();
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str: strs) {
            String key = isAnagram(str);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(str);
        }
        return new ArrayList<>(map.values());
    }
}
