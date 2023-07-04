class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uniqueNums;
        for (int num : nums) {
            if (uniqueNums.count(num) > 0) 
                return true;
            uniqueNums.insert(num);
        }
        return false;
    }
};
