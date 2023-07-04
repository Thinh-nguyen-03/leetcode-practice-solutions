class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> counts;  
        int sum = 0, count = 0; 
        for (auto num : nums) {
            sum += num;  
            if (sum == k)  
                count++;
            if (counts.find(sum - k) != counts.end())  
                count += counts[sum - k]; 
            counts[sum]++; 
        }
        return count;  
    }
};
