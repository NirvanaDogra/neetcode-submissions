class Solution {
    public boolean isAnagram(String s, String t) {
        s = s.toLowerCase();
        t = t.toLowerCase();
        if(s.length() != t.length()) {
            return false;
        }
        int[] ar1 = new int[29];
        int[] ar2 = new int[29];
        for(int i=0; i<29; i++) {
            ar1[i] = 0;
            ar2[i] = 0;
        }

        for (int i = 0; i < s.length(); i++) {
            ar1[s.charAt(i) - 'a']++;
            ar2[t.charAt(i) - 'a']++;
        }
        System.out.println("ar1 contents: " + Arrays.toString(ar1));
        System.out.println("ar2 contents: " + Arrays.toString(ar2));
       
        for(int i=0; i<29; i++) {
            if (ar1[i] != ar2[i]) {
                return false;
            }
        }
        return true;

    }
}
