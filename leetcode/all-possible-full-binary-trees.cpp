#include <bits/stdc++.h>
using namespace std;

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
    vector<TreeNode *> allPossibleFBT(int n)
    {
        if (n % 2 == 0)
            return vector<TreeNode *>{};
        return recur(n);
    }

    vector<TreeNode *> recur(int n)
    {
        vector<TreeNode *> result;
        if (n == 1)
        {
            TreeNode *root = new TreeNode(0);
            result.push_back(root);
            return result;
        }
        for (int i = 1; i < n; i += 2)
        {
            auto leftNodes = recur(i);
            auto rightNodes = recur(n - i - 1);

            for (auto leftnode : leftNodes)
            {
                for (auto rightnode : rightNodes)
                {
                    TreeNode *root = new TreeNode(0, leftnode, rightnode);
                    result.push_back(root);
                }
            }
        }
        return result;
    }
};