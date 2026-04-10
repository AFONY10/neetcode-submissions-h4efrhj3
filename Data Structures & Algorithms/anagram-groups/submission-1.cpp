class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Declare a map where key is the sorted string and value is a vector of anagrams
        unordered_map<string, vector<string>> ana_map;

        // Iterate through each string in the input vector
        for (const string& s : strs) {
            // Sort the string to form the key
            string key = s;
            sort(key.begin(), key.end());

            // Add the original string to the vector corresponding to the sorted key
            ana_map[key].push_back(s);
        }

        // Prepare the result vector
        vector<vector<string>> result;
        for (const auto& pair : ana_map) {
            result.push_back(pair.second);
        }

        return result;
    }
};
