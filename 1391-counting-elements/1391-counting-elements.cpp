class Solution {
public:
    int countElements(vector<int>& arr) {
        unordered_map<int, int> map;
        for (int num : arr) 
            map[num]++;
        int count = 0;
        for (auto& elem : map) {
            // If x + 1 exists in the map, add the count of x to the total count.
            if (map.find(elem.first + 1) != map.end()) 
                count += elem.second;
        }
        return count;
    }
};
