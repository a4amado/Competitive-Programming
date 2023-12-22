/*
 * @lc app=leetcode id=67 lang=cpp
 *
 * [67] Add Binary
 */
#include <math.h>

#include <algorithm>
#include <cstring>
#include <iostream>
#include <numbers>
#include <string>
#include <vector>

using namespace std;

// @lc code=start

class Solution {
 public:
  string addBinary(string a, string b) {
    bool a_bad = true;
    for (int i = 0; i < a.length(); i++) {
      if (a.at(i) - '0' > 0) {
        a_bad = false;
        break;
      }
    }
    if (a_bad) {
      return b;
    }

    bool b_bad = true;
    for (int i = 0; i < b.length(); i++) {
      if (b.at(i) - '0' > 0) {
        b_bad = false;
        break;
      }
    }
    if (b_bad) {
      return a;
    }
    reverse(a.begin(), a.end());

    reverse(b.begin(), b.end());

    int carry = -1;

    string final = "";

    for (int i = 0; i <= max(a.length(), b.length()); i++) {
      vector<int> q;
      int aa = i < a.length() ? a[i] - '0' : 0;
      int bb = i < b.length() ? b[i] - '0' : 0;

      if (aa == 1) {
        q.push_back(1);
      }
      if (bb == 1) {
        q.push_back(1);
      }
      if (carry == 1) {
        q.push_back(1);
      }

      if (q.size() == 3) {
        final.push_back('1');
        carry = 1;
        continue;
      }

      if (q.size() == 2) {
        final.push_back('0');
        carry = 1;
        continue;
      }
      if (q.size() == 1) {
        final.push_back('1');
        carry = -1;
        continue;
      }
      if (q.size() == 0 && i != max(a.length(), b.length())) {
        final.push_back('0');
        carry = -1;
      }
    }

    reverse(final.begin(), final.end());

    return final;
  }
};

// @lc code=end
