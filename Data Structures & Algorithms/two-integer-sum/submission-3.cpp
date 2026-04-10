class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int,int> resMap;

        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];

            if(resMap.find(complement) != resMap.end()){

                return{resMap[complement], i};
            }
            
            resMap[nums[i]]=i;
        }
        
        return{};
    }
};
