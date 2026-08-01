class Solution {
    public boolean isPalindrome(String text) {
        StringBuilder sb = new StringBuilder();
        for(char t: text.toCharArray()) {
            if (!((t >= 'A' && t <= 'Z') || 
                  (t >= 'a' && t <= 'z') || 
                  (t >='0' && t <='9')) 
                ) {
                continue;
            }
            sb.append(t);
        }
        String s = sb.toString().toLowerCase();
        System.out.println(s);
        int lp = 0;
        int rp = s.length()-1;
        while(rp >= 0 && lp < s.length()) {
            // should be same
            if (s.charAt(rp) == s.charAt(lp)) {
                rp--;
                lp++;
            } else {
                return false;
            }
        }
        return true;
    }
}
