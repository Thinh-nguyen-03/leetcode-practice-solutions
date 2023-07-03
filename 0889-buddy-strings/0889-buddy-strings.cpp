class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()) {
            return false;
        }
        if (s == goal) {
            int letters[26] = {0};
            for (char c : s) {
                if (++letters[c - 'a'] > 1) {
                    return true;
                }
            }
            return false;
        } else {
            int count = 0;
            pair<int, int> diff;
            for (int i = 0; i < s.size(); ++i) {
                if (s[i] != goal[i]) {
                    ++count;
                    if (count > 2) {
                        return false;
                    }
                    if (count == 1) {
                        diff.first = i;
                    } else {
                        diff.second = i;
                    }
                }
            }
            return count == 2 && s[diff.first] == goal[diff.second] && s[diff.second] == goal[diff.first];
        }
    }
};
