class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int size = nums.size(), win_size = k * 2 + 1;
        vector<int> ans(size, -1); 
        long long sum[size + 1]; 
        sum[0] = nums[0];
        for (int i = 0; i < size; i++) {
            sum[i + 1] = sum[i] + nums[i];
        }
        for (int i = k; i + k < size; i++) {
            ans[i] = (sum[i + k + 1] - sum[i - k]) / win_size;
        }
        return ans;
    }
};