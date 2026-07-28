class Solution {
    // o(str)
    private String getCharFreqArray(String str) {
        int ar[] = new int[29];
        for(int i = 0; i<29; i++){
            ar[i] = 0;
        }
        for(char c: str.toCharArray()) {
            ar[c - 'a']++;
        }
        return Arrays.toString(ar);
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str: strs) { 
            String encodedStr = getCharFreqArray(str);
            map.putIfAbsent(encodedStr, new ArrayList());
            map.get(encodedStr).add(str);
        }
        return new ArrayList<>(map.values());
    }
}
