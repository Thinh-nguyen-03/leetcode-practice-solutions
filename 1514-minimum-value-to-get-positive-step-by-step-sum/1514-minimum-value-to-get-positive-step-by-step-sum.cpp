class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int prefix_sum = 0;
        int min_prefix_sum = 0;
        for(int num: nums) {
            prefix_sum += num;
            min_prefix_sum = min(prefix_sum, min_prefix_sum);
        }
        return std::max(1 - min_prefix_sum, 1);
    }
};