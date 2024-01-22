#include <iostream>
#include <vector>

using namespace std;

int main()
{

    return 0;
};

class TreeNode
{
public:
    TreeNode(int v) : val(v), left(nullptr), right(nullptr), parent(nullptr){};

    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    bool isLeaf() {
        return this->left == NULL && this->right == NULL;
    }
};
class Tree
{
private:
    TreeNode *root;
    TreeNode *insertRecursive(TreeNode *sub_tree_head, int val)
    {
        if (sub_tree_head == NULL)
        {
            return new TreeNode(val);
        };
        if (val < sub_tree_head->val)
        {
            sub_tree_head->left = this->insertRecursive(sub_tree_head->left, val);
            sub_tree_head->left->parent = sub_tree_head;
        }
        else
        {
            sub_tree_head->right = this->insertRecursive(sub_tree_head->right, val);
            sub_tree_head->right->parent = sub_tree_head;
        }
    }

    TreeNode *maxInTree(TreeNode *node)
    {
        while (node->right != NULL)
        {
            node = node->right;
        }
        return node;
    }

    TreeNode *minInTree(TreeNode *node)
    {
        while (node->left != NULL)
        {
            node = node->left;
        }
        return node;
    }

    TreeNode *predecessor(TreeNode *node)
    {
        // max in left node
        if (node->left)
            return this->minInTree(node->left);
        // or [parent] if currunt node is right child for it's parent
        if (node->parent && node == node->parent->right)
            return node->parent;
        // or first right child ancestor
        while (node->parent && node->parent->right != node)
        {
            node = node->parent;
        }
        return node->parent;
    }

    TreeNode *successor(TreeNode *node)
    {
        if (node->right)
            return this->minInTree(node->right);
        if (node->parent && node == node->parent->left)
            return node->parent;
        while (node->parent && node->parent->left != node)
        {
            node = node->parent;
        }
        return node->parent;
    }

    TreeNode *swapNode(TreeNode *node1, TreeNode *node2)
    {
        node1->val = node2->val;
        return node2;
    }

    void removeNode(TreeNode *node)
    {
        // if node is a leaf
        if (node->left == NULL && node->right == NULL)
        {
            // if node is a right child ? nullift right pointer
            if (node == node->parent->right)
                node->parent->right = nullptr;
            // if node is a left child ? nullift left pointer
            else
                node->parent->left = nullptr;
            // nullift node memory
            delete node;
            node = NULL;
            return;
        }

        // [ALERT] Turnury operator to avoid the if/else statement
        TreeNode *node_to_be_swaped = (node->right != NULL ? this->successor(node) : this->predecessor(node));
        TreeNode *node_to_be_deleted = this->swapNode(node, node_to_be_swaped);
        return this->removeNode(node_to_be_deleted);
    }
    
    TreeNode *findRecursive(int val, TreeNode *node)
    {
        // base case
        // if not found
        if (node == NULL)
            return NULL;

        // if found
        if (node->val == val)
            return node;
        // if a leaf and not equal to val
        if (node->left == NULL && node->right == NULL && val != node->val)
            return NULL;
        // if no right child and val is greater ? retutn Null
        if (node->right == NULL && val > node->val)
            return NULL;
        // if no left child and val is less ? retutn Null
        if (node->left == NULL && val < node->val)
            return NULL;

        TreeNode *next_sub_tree = (val > node->val ? node->right : node->left);
        return this->findRecursive(val, next_sub_tree);
    }
    bool toLeaf(TreeNode* root, vector<int> path) {
        if (root == NULL || root->val==0) return false;
        path.push_back(root->val);
        // if leaf
        if (root->isLeaf()) return true;
        if (this->toLeaf(root->left, path)) return true;
        if (this->toLeaf(root->right, path)) return true;
        path.pop_back();
        return false;
    };
public:
    Tree() : root(nullptr){};
    TreeNode *insert(int val)
    {
        if (this->root == nullptr)
        {
            this->root = new TreeNode(val);
            return;
        }
        return this->insertRecursive(this->root, val);
    };
    void *deleteNode(int v)
    {
        TreeNode *to_be_deleted = this->find(v);
        this->removeNode(to_be_deleted);
    }

    TreeNode *find(int v)
    {
        return this->findRecursive(v, root);
    }
};