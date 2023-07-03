class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Sort the input array.
        sort(nums.begin(), nums.end());  
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size(); i++) {
            // Ignore the same number to avoid duplicate triplets.
            if (i > 0 && nums[i] == nums[i-1]) 
                continue;
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    ans.push_back({nums[i], nums[j], nums[k]});
                    // Skip the same numbers from j to avoid duplicate triplets.
                    while (j < k && nums[j] == nums[j+1]) 
                        j++;
                    // Skip the same numbers from k to avoid duplicate triplets.
                    while (j < k && nums[k] == nums[k-1])  
                        k--;
                    // Move both pointers inward.
                    j++; k--;
                } 
                // If the sum < 0, move j to the right.
                else if (sum < 0) 
                    j++;
                // If the sum > 0, decrease k to the left.
                else
                    k--;
            }
        }
        // Return the result vector.
        return ans;
    }
};
