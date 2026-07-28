class Solution {
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
        Map<String, List<String>> map = new HashMap();
        for(String str: strs) {
            String encodedStr = getCharFreqArray(str);
            if(map.containsKey(encodedStr)) {
                map.get(encodedStr).add(str);
            } else {
                map.put(encodedStr, new ArrayList(List.of(str)));
            }
        }
        return map.values().stream().toList();
    }
}
