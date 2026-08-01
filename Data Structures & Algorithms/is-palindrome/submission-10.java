class Solution {
    public boolean isPalindrome(String text) {
        int lp = 0;
        int rp = text.length()-1;
        while(lp < rp) {
            char leftChar = text.charAt(lp);
            char rightChar = text.charAt(rp);

            if (!Character.isLetterOrDigit(leftChar)) {
                lp++;
                continue;
            }

            if (!Character.isLetterOrDigit(rightChar)) {
                rp--;
                continue;
            }
            // should be same
            if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                return false;
            }

            lp++;
            rp--;
        }
        return true;
    }
}
