// https://leetcode.com/problems/total-cost-to-hire-k-workers/
#include <bits/stdc++.h>
using namespace std;

struct compare
{
    bool operator()(pair<int, int> &a, pair<int, int> &b)
    {
        if (a.first == b.first)
        {
            return a.second > b.second;
        }
        else
        {
            return a.first > b.first;
        }
    }
};

// void printpq(priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq)
// {
//     auto temp = pq;
//     while (!temp.empty())
//     {
//         printf("<%d,%d>,", temp.top().first, temp.top().second);
//         temp.pop();
//     }
//     printf("\n");
// }

class Solution
{
public:
    long long totalCost(vector<int> &costs, int k, int candidates)
    {
        int left = 0, right = costs.size() - 1;
        long long answer = 0L;
        priority_queue<pair<int, int>, vector<pair<int, int>>, compare> heap;
        while (left < candidates)
        {
            pair<int, int> p = {costs[left], left};
            heap.push(p);
            left++;
        }

        int temp = costs.size();
        int a = max(left, temp - 1 - candidates);
        while (a < right)
        {
            pair<int, int> p = {costs[right], right};
            heap.push(p);
            right--;
        }
        // printpq(heap);
        // printf("%d,%d\n", left, right);

        while (k)
        {
            pair<int, int> p = heap.top();
            heap.pop();
            answer += (long long)p.first;

            if (left > right)
            {
            }
            else if (abs(p.second - left) < abs(p.second - right))
            {
                pair<int, int> p = {costs[left], left};
                heap.push(p);
                left++;
            }
            else
            {
                pair<int, int> p = {costs[right], right};
                heap.push(p);
                right--;
            }

            k--;
        }
        return answer;
    }
};