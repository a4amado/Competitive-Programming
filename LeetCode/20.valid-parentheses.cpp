/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */
#include <iostream>
using namespace std;
#include <string>
#include <stack>

// @lc code=start
class Solution
{
public:

char opposite_of(char aa)
{

    if (aa == '{')
    {
        return '}';
    }
    else if (aa == '[')
    {
        return ']';
    }
    else
    {
        return ')';
    }
    return aa;
}
bool isValid(string s)
{
    if (s.size() % 2 != 0)
    {
        return false;
    }

    stack<char> ss;

    for (int i = 0; i < s.size(); i++)
    {
        if (i == 0 || ss.size() == 0 )
        {
            if (s.at(i) == ']' || s.at(i) == '}' || s.at(i) == ')')
            {
                return false;
            }
            else
            {
                ss.push(s.at(i));
            }
        }






















        else if (i == s.size() - 1)
        {
            if (ss.size() > 1) { 
                return false;
            }
            char rr = s.at(i);
            bool g = rr != ')';
            bool h = rr != '}';
            bool k = rr != ']';
            if (h && k && g)
            {
                return false;
            }

            char top = opposite_of(ss.top());
            char curr = s.at(i);

            if (top != curr)
            {
                return false;
            }
        }
        else
        {
            if (s.at(i) == '[' || s.at(i) == '{' || s.at(i) == '(')
            {
                ss.push(s.at(i));
            }
            else
            {

                char top = opposite_of(ss.top());
                char curr = s.at(i);

                if (top != curr)
                {
                    return false;
                } else {
                    ss.pop();
                }
            }
        }
    }

    return true;
}


};
// @lc code=end
