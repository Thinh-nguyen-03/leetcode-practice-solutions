class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> counts; 
        int ans = 0, count = 0;  
        for (auto num : nums) {
            count += num % 2;
            if (count == k) 
                ans++;
            if (counts.find(count - k) != counts.end())  
                ans += counts[count - k];  
            counts[count]++;  
        }
        return ans;  
    }
};
