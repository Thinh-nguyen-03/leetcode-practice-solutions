class Solution {
public:
    int missingNumber(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int expectedNumCount = nums.size() + 1;
        for (int number = 0; number < expectedNumCount; number++) {
            if (numSet.find(number) == numSet.end()) {
                return number;
            }
        }
        return -1;
    }
};
