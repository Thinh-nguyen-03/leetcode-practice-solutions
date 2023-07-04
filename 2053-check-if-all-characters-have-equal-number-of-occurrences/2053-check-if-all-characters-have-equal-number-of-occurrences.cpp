class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char,int> freq;
        for(auto i : s)
            freq[i]++;
        int val = freq[s[0]];
        for(auto i : freq)
            if(i.second != val)
                return false;
        return true;
    }
};