class Solution {
public:
    void reverseString(vector<char>& s) {
        unsigned int i = s.size() - 1;
        unsigned int j = 0;
        while (j < i)
        {
            swap(s[i], s[j]);
            i--; j++;
        }
    }
};