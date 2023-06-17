class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        unsigned int l = 0;
        unsigned int r = nums.size() - 1;
        unsigned int k = nums.size() - 1;
        while(l <= r) {
            if(abs(nums[l]) < abs(nums[r])) {
                res[k] = nums[r] * nums[r];
                r--;
            }
            else {
                res[k] = nums[l] * nums[l];
                l++;
            }
            k--;
        }
        return res;
    }
};