#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int partitionString(string s) {
        int count = 0;
        unordered_map<char, int> mm;
        
        for (char c:s) {
            if (mm.find(c) == mm.end()) {
                mm.emplace(c, 1);
            } else {
                count++;
                mm.clear();
                mm.emplace(c, 1);
            }
        }
        if (mm.size() == 0) {
        return count;    
        }
        return count + 1;
        
    }
};
