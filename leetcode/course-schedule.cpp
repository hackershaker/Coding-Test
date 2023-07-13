#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<int> indegree(numCourses, 0);
        unordered_map<int, vector<int>> graph;
        for (auto v : prerequisites)
        {
            indegree[v[0]]++;
            graph[v[1]].push_back(v[0]);
        }

        deque<int> queue;
        for (int i = 0; i < numCourses; i++)
        {
            if (indegree[i] == 0)
                queue.push_back(i);
        }

        int num = 0;
        while (!queue.empty())
        {
            auto node = queue.front();
            queue.pop_front();
            num++;
            for (auto nextNode : graph[node])
            {
                indegree[nextNode]--;
                if (indegree[nextNode] == 0)
                    queue.push_back(nextNode);
            }
        }

        return ((num == numCourses) ?  true :  false);
    }
};