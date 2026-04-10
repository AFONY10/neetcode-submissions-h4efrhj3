class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lp = 0;
        int rp = 0;
        int maxSubString = 0;
        HashSet<Character> uniqueChars = new HashSet<Character>();

        while(rp < s.length()){
            while(uniqueChars.contains(s.charAt(rp))){
                uniqueChars.remove(s.charAt(lp));
                lp++;
            }

            uniqueChars.add(s.charAt(rp));
            int currentSubString = rp - lp + 1;
            if(currentSubString > maxSubString){
                maxSubString = currentSubString;
            }
            rp++;
        }

        return maxSubString;
    }
}
