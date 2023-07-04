class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> freq;  
        for (auto i : s) 
            freq[i]++;  // Increment the frequency of the current character in the map.
        int val = freq[s[0]];  
        for (auto i : freq)  
            // If the frequency of any character != the frequency of the 1st character
            if (i.second != val)  
                return false;  
        return true;  
    }
};
