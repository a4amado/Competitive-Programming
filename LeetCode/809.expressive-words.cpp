#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int expressiveWords(string s, vector<string> &words)
    {

        vector<string> s_d = this->divide(s);
        int count = 0;
        for (string word : words)
        {
            vector<string> i_d = this->divide(word);
            if (s_d.size() != i_d.size())
                continue;
            int vaild = 0;
            for (int i = 0; i < s_d.size(); i++)
            {
                string item_sub_str = i_d[i];
                string stretch_sub_str = s_d[i];
                if (item_sub_str[0] != stretch_sub_str[0])
                {
                    i = s_d.size();
                    continue;
                };
                if (item_sub_str.length() > stretch_sub_str.length())
                {
                    i = s_d.size();
                    continue;
                }

                if (item_sub_str.length() == 1 && stretch_sub_str.length() == 2)
                {
                    i = s_d.size();
                    continue;
                }
                vaild++;
            }
            if (vaild == s_d.size())
            {
                count++;
            }
        }
        return count;
    }
    vector<string> divide(string s)
    {
        vector<string> l;
        for (int i = 0; i < s.length();)
        {
            string sub_str;
            int j = i;
            bool inital = true;
            while (inital)
            {
                if (sub_str.length() == 0)
                {
                    sub_str.push_back(s.at(j));
                    j++;
                }
                else if (sub_str.back() == s[j])
                {
                    sub_str.push_back(s.at(j));
                    j++;
                }
                else
                {
                    inital = false;
                    i = j;
                }
            }

            l.push_back(sub_str);
        }
        return l;
    }
};

int main()
{
    Solution s = Solution();
    vector<string> sssss = {"zzyy", "zy", "zyy"};
    cout << s.expressiveWords("zzzzzyyyyy", sssss) << endl;
    return 0;
}