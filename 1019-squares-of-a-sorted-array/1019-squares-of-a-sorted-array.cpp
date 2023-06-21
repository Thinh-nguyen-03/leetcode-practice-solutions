class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        
        int start = 0;
        int end = n - 1;
        
        for (int i = n - 1; i >= 0; i--) {
            int square;
            
            if (abs(nums[start]) > abs(nums[end])) {
                square = nums[start] * nums[start];
                start++;
            } else {
                square = nums[end] * nums[end];
                end--;
            }
            
            res[i] = square;
        }
        
        return res;
    }
};
