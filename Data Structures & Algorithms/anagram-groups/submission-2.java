class Solution {
    private String getHash(String s) {
        int[] ar = new int[26];
        Arrays.fill(ar, 0);

        for(char ch: s.toCharArray()) {
            int index = (int)ch - (int)'a';
            ar[index]+=1;
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<26; i++) {
            sb.append(ar[i]);
            sb.append("#");
        }

        return sb.toString();
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>() ;
        for(String str: strs) {
            String key = getHash(str);
            if(map.containsKey(key)) {
                map.get(key).add(str);
            } else {
                map.put(key, new ArrayList<String>());
                map.get(key).add(str);
            }
        }

        return map.values().stream().toList();
    }
}
