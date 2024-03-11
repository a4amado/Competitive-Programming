#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Node
{
public:
    int val;
    vector<Node *> neighbors;
    Node()
    {
        val = 0;
        neighbors = vector<Node *>();
    }
    Node(int _val)
    {
        val = _val;
        neighbors = vector<Node *>();
    }
    Node(int _val, vector<Node *> _neighbors)
    {
        val = _val;
        neighbors = _neighbors;
    }
};



class Solution
{
public:
    Node *cloneGraph(Node *node)
    {
        if (node == nullptr)
            return node;

        unordered_map<int, Node *> tracker;

        Node *head = new Node(node->val);
        tracker.insert({head->val, head});

        for (auto item : node->neighbors)
        {
            Node* i = this->dfs(item, head, &tracker);
            head->neighbors.push_back(i);
        }

        return head;
    }

    Node *dfs(Node *node, Node *head, unordered_map<int, Node *> *tracker)
    {
        if (node == nullptr)
            return node;
        // does currunt node exist ?
        // yes. skip
        // no. create it
        //     then
        //     1. insert it
        //     2. add it to the
        auto node_exist = tracker->find(node->val);

        if (node_exist != tracker->end())
        {
            return node_exist->second;
        };

        Node *new_node = new Node(node->val);


        tracker->insert({new_node->val, new_node});

        if (node->neighbors.size() == 0)
        {
            return new_node;
        }

        // for node->neighbors
        // loop over them
        // does it exist ?
        // yes. -> get it's ptr from the hashmap and add it
        // no. -> create it add it, add it to the hashmap
        for (Node *neighbor : node->neighbors)
        {
            bool neighbor_exist = tracker->find(neighbor->val) != tracker->end();
            if (neighbor_exist)
            {
                auto neighbor_ptr = tracker->find(neighbor->val);
                new_node->neighbors.push_back(neighbor_ptr->second);
            }
            else
            {
                Node *new_neighbor = this->dfs(neighbor, new_node, tracker);
                if (new_node && new_neighbor)
                {
                    new_node->neighbors.push_back(new_neighbor);
                }
            }
        }

        return new_node;
    }
};

 