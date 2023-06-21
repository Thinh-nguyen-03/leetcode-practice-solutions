class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        long long size = nums.size();
        vector<int> ans(size, -1); 
        vector<long long> sum(size + 1); 
        if (size < k * 2 + 1) {
            return ans;
        }
        for (int i = 0; i < size; i++) {
            sum[i + 1] = sum[i] + nums[i];
        }
        for (int i = k; i + k < size; i++) {
            ans[i] = (sum[i + k + 1] - sum[i - k]) / (k * 2 + 1);
        }
        return ans;
    }
};