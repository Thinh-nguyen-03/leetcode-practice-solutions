class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int comp = target - num;
            if (map.find(comp) != map.end()) 
                return {i, map[comp]};
            map[num] = i;
        }
        return {-1, -1};
    }
};