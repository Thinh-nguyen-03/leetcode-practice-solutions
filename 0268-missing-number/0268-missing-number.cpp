class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0,n = nums.size();
        for(int i = 0; i < n; i++)
            sum += nums[i];
        // Gauss' formula
        // The missing number is the difference
        return ((n * (n + 1)) / 2) - sum;
    }
};
