// https://leetcode.com/problems/minimum-cost-to-make-array-equal/
#include <bits/stdc++.h>
using namespace std;

// 절댓값 함수의 합의 최솟값 -> median
// 그런데 weighted되어 있으므로 cost의 반 값으로 median을 찾는다
// ex) 2|x-1|+5|x-4|+3|x-8|
//  1 1 4 4 4 4 4 8 8 8 -> median = 4

class Solution
{
public:
    long long minCost(vector<int> &nums, vector<int> &cost)
    {
        vector<pair<int, int>> arr;
        int i = 0;
        long long int answer = 0, eqNum = 0, temp = 0;
        long long int costSum = accumulate(cost.begin(), cost.end(), 0LL);
        for (i = 0; i < nums.size(); i++)
        {
            pair<int, int> p(nums[i], cost[i]);
            arr.push_back(p);
        }

        sort(arr.begin(), arr.end());

        for (i = 0; i < nums.size(); i++)
        {
            temp += arr[i].second;
            if (costSum % 2 == 1 && temp >= (costSum / 2) + 1 || costSum % 2 == 0 && temp >= (costSum / 2))
            {
                eqNum = arr[i].first;
                break;
            }
        }

        for (i = 0; i < nums.size(); i++)
        {
            answer += abs(eqNum - (long long int)nums[i]) * (long long int)cost[i];
        }
        return answer;
    }
};