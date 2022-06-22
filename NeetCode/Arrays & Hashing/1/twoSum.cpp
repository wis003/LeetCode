class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> temp;
        unordered_map<int,int> map;
        for (int i = 0; i < nums.size(); i++) {
            map.insert({nums[i], i});
        }
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            auto search = map.find(complement);
            if (search != map.end()) {
                if(i != search->second) {
                    temp.push_back(i);
                    temp.push_back(search->second);
                    return temp;
                }
            }
        }
        return temp;
    }
};