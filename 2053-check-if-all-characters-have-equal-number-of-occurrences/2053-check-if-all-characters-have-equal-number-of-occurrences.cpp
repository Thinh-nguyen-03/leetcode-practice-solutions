class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> count;
        for (char c: s) 
            count[c]++;
        unordered_set<int> freq;
        for (auto [key, val]: count) 
            freq.insert(val);
        return freq.size() == 1;
    }
};