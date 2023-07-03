class Solution {
public:
    bool checkIfPangram(string sentence) {
        array<bool, 26> seen{};
        for (auto currChar : sentence)
            seen[currChar - 'a'] = true;
        for (auto status : seen)
            if (!status)
                return false;
        return true;

        /* Using set
        unordered_set<char> seen(sentence.begin(), sentence.end());
        return seen.size() == 26; */
    }
};