class Solution {
    Map<String, Boolean> memo = new HashMap<>();
    Boolean dfs(String s, List<String> wordDict) {
        if(s.length() == 0) {
            return true;
        }
        if (memo.containsKey(s)) {
            return memo.get(s);
        }
        for(String word: wordDict) {
            if (s.length() >= word.length() && s.substring(0, word.length()).equals(word)) {
                String unCheckedStr = s.substring(word.length(), s.length());
                
                if (dfs(unCheckedStr, wordDict)) {
                    memo.put(s, true);
                    return true;
                }

            }   
        }
        memo.put(s, false);
        return false;
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(s, wordDict);
    }
}
