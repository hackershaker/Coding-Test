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
#include <bits/stdc++.h>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int minDepth(TreeNode *root)
    {
        if (!root)
            return 0;
        int answer = 100000;
        vector<tuple<TreeNode *, int>> stack;
        stack.push_back({root, 1});

        while (!stack.empty())
        {
            auto t = stack.back();
            stack.pop_back();
            auto node = get<0>(t);
            auto depth = get<1>(t);

            if (!(node->left) && !(node->right))
            {
                answer = min(answer, depth);
                continue;
            }

            if (node->left)
            {
                stack.push_back({node->left, depth + 1});
            }
            if (node->right)
            {
                stack.push_back({node->right, depth + 1});
            }
        }
        return answer;
    }
};