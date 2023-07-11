// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    vector<int> distanceK(TreeNode *root, TreeNode *target, int k)
    {
        unordered_map<int, vector<int>> graph;
        makeGraph(graph, root);

        vector<int> stack = {target->val};
        unordered_set<int> visited = {};
        int distance = 0;

        if (distance == k)
            return stack;

        while (!stack.empty())
        {
            for (auto k : stack)
            {
                printf("%d,", k);
            }
            printf("\n");
            vector<int> newStack;
            distance += 1;
            for (auto node : stack)
            {
                visited.insert(node);
                for (auto nextnode : graph[node])
                {
                    if (visited.find(nextnode) == visited.end())
                    {
                        newStack.push_back(nextnode);
                    }
                }
            }

            if (distance == k)
                return newStack;
            else
                stack = newStack;
        }
        return stack;
    }

    void makeGraph(unordered_map<int, vector<int>> &graph, TreeNode *root)
    {
        if (root->left)
        {
            graph[root->val].push_back(root->left->val);
            graph[root->left->val].push_back(root->val);
            makeGraph(graph, root->left);
        }
        if (root->right)
        {
            graph[root->val].push_back(root->right->val);
            graph[root->right->val].push_back(root->val);
            makeGraph(graph, root->right);
        }
    }
};