class Solution
{
public:
    void findAllPaths(TreeNode *root, vector<int> &curruntPath, vector<vector<int>> &list_of_paths ) {
        if (root == nullptr) return;
        curruntPath.push_back(root->val);
        // if leaf
        if (root->left == nullptr && root->right == nullptr) {
            list_of_paths.push_back(curruntPath);
        };
        this->findAllPaths(root->left, curruntPath, list_of_paths);
        this->findAllPaths(root->right, curruntPath, list_of_paths);


        curruntPath.pop_back();
        return;
    }
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        vector<int> curruntPath;
        vector<vector<int>> list_of_paths;
        this->findAllPaths(root, curruntPath, list_of_paths);
        for (auto it: list_of_paths) {
            int val = accumulate(it.begin(), it.end(), 0);
            if (val == targetSum) return true;
        }
        return false;
    }
};
