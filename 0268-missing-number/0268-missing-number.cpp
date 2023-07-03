class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int total = n * (n + 1) / 2; // Gauss' formula
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return total - sum; // The missing number is the difference
    }
};
