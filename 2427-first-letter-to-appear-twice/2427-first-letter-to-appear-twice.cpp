class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_set<char> appeared;
        for (char c: s) {
            if (appeared.find(c) != appeared.end()) 
                return c;
            appeared.insert(c);
        }
        return ' ';
    }
};