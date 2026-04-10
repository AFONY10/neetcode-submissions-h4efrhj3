class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> intCounter;

        // 1. Insert all numbers in map by occurence
        for(const auto& num : nums){
            intCounter[num]++;
        }

        // 2. Priority queue to sort map values in descending order
        priority_queue<pair<int,int>> pq;
        for(const auto& pair : intCounter){
            pq.push({pair.second,pair.first});
        }

        // 3. Insert pq in result-vector
        vector<int> result;
        for(int i = 0; i < k; ++i){
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};
