/*
 * @lc app=leetcode id=1022 lang=cpp
 *
 * [1022] Sum of Root To Leaf Binary Numbers
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// struct TreeNode
// {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution
{
public:
    int sumRootToLeaf(TreeNode *root)
    {
        if (root == nullptr)
            return 0;
        int nums = 0;

        string c = "";
        
        this->allPaths(nums, c, root);
        
        return nums;
    }

    void allPaths(int &nums, string currunt_string, TreeNode *node)
    {
        if (node == nullptr)
            return;

        currunt_string.push_back(node->val + '0');
        if (this->isLeaf(node))
        {
            nums += this->binaryToDecimal(currunt_string);
            return;
        }
        this->allPaths(nums, currunt_string, node->left);

        this->allPaths(nums, currunt_string, node->right);

    }

    bool isLeaf(TreeNode *node)
    {
        if (node == nullptr)
            return false;
        if (node->left == nullptr && node->right == nullptr)
            return true;
        return false;
    }
    int binaryToDecimal(const std::string &binaryString)
    {
        int decimalNumber = 0;
        int exponent = 0;

        for (int i = binaryString.length() - 1; i >= 0; --i)
        {
            if (binaryString[i] == '1')
            {
                // If the current bit is '1', add 2^exponent to the decimal number
                decimalNumber += static_cast<int>(std::pow(2, exponent));
            }
            // Increment the exponent for the next bit
            ++exponent;
        }

        return decimalNumber;
    }
};

// @lc code=end
