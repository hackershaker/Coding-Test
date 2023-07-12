// https://leetcode.com/problems/find-eventual-safe-states/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> eventualSafeNodes(vector<vector<int>> &graph)
    {
        vector<int> dp(graph.size(), -1);
        vector<int> answer;
        for (int i = 0; i < dp.size(); i++)
        {
            if (dp[i] == -1)
            {
                unordered_set<int> visited;
                dp[i] = isTerminal(i, dp, graph, visited);
            }
        }

        for (int i = 0; i < dp.size(); i++)
        {
            // printf("dp[%d]:%d\n", i, dp[i]);
            if (dp[i] == 1 || graph[i].size() == 0)
                answer.push_back(i);
        }
        return answer;
    }

    int isTerminal(int n, vector<int> &dp, vector<vector<int>> &graph, unordered_set<int> &visited)
    {
        if (graph[n].size() == 0)
        {
            dp[n] = 1;
            return 1;
        }
        if (visited.find(n) != visited.end())
        {
            dp[n] = 0;
            return 0;
        }

        visited.insert(n);

        for (auto next : graph[n])
        {
            if (dp[next] == -1)
            {
                dp[next] = isTerminal(next, dp, graph, visited);
            }
            if (dp[next] == 0)
            {
                dp[n] = 0;
                visited.erase(n);
                return 0;
            }
        }
        dp[n] = 1;
        visited.erase(n);
        return 1;
    }
};