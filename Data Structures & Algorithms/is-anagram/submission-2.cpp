class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        unordered_map<char,int> charCount;

        for(char c : t){
            charCount[c]++;
        }

        for(char c : s){

            if(charCount[c] == 0)
                return false;
            
            charCount[c]--;
        }
        
        return true;
    }
};
