class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& num) {
        sort(num.begin(), num.end());
        vector<vector<int>> ans;
        for(int i = 0; i < num.size(); i++) {
            if (i > 0 && num[i] == num[i - 1])
                continue;
            int j = i + 1, k = num.size() - 1;
            while (j < k) {
                int sum = num[i] + num[j] + num[k];
                if (sum == 0) {
                    ans.push_back({num[i], num[j], num[k]});
                    while (j < k && num[j] == num[j + 1])
                        j++;
                    while (j < k && num[k] == num[k - 1])
                        k--;
                    j++;
                    k--;    
                }
                else if (sum < 0) 
                    j++;
                else
                    k--;
            }
        }
    return ans;
    }
};
