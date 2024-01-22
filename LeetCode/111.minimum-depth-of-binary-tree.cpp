/*
 * @lc app=leetcode id=111 lang=cpp
 *
 * [111] Minimum Depth of Binary Tree
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
#include <iostream>
#include <vector>
#include <queue>

// struct TreeNode
// {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

using namespace std;

class Solution
{
public:
    int minDepth(TreeNode *root)
    {
        if (root == nullptr)
            return 0;

        priority_queue<int, vector<int>, greater<int>> min;

        int curr = 0;

        this->allPaths(&min, curr, root);

        return min.top();
    }

    void allPaths(priority_queue<int, vector<int>, greater<int>> *que, int currunt_count, TreeNode *node)
    {
        if (node == nullptr)
            return;

        if (this->isLeaf(node))
        {
            que->push(currunt_count + 1);
            return;
        }

        this->allPaths(que, currunt_count + 1, node->left);
        this->allPaths(que, currunt_count + 1, node->right);
    }
    bool isLeaf(TreeNode *node)
    {
        if (node == nullptr)
            return false; // It's not a leaf if the node is null
        if (node->left == nullptr && node->right == nullptr)
            return true;
        return false;
    }
};

// @lc code=end
