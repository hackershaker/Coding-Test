// https://leetcode.com/problems/path-with-maximum-probability/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double maxProbability(int n, vector<vector<int>> &edges, vector<double> &succProb, int start, int end)
    {
        double answer = 1.0;
        double memo[n];
        fill_n(memo, n, 0.0);
        unordered_map<int, vector<pair<int, double>>> dic;
        deque<int> stack = {start};
        for (int i = 0; i < edges.size(); i++)
        {
            dic[edges[i][0]].push_back({edges[i][1], succProb[i]});
            dic[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        memo[start] = 1.0;
        while (!stack.empty())
        {
            int node = stack[0];
            stack.pop_front();
            if (node == end)
            {
                continue;
            }

            for (auto next : dic[node])
            {
                if (next.second * memo[node] > memo[next.first])
                {
                    memo[next.first] = next.second * memo[node];
                    stack.push_back(next.first);
                }
            }
        }
        return memo[end];
    }
};