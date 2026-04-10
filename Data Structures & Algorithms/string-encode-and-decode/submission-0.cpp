class Solution {
public:

    string encode(vector<string>& strs) {
        string r_string;
        for(const auto& s : strs){
            r_string += to_string(s.size()) + ":" + s;
        }

        return r_string;
    }

    vector<string> decode(string s) {
        vector<string> result;

        int i = 0;
    while (i < s.size()) {
        // Find the position of the next delimiter
        int colon = s.find(':', i);
        // Get the length of the next string
        int length = stoi(s.substr(i, colon - i));
        // Extract the string of the specified length
        string str = s.substr(colon + 1, length);
        // Add the string to the result vector
        result.push_back(str);
        // Move the index to the next string segment
        i = colon + 1 + length;
    }
    return result;


    }
};
