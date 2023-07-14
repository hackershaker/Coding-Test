// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestSubsequence(vector<int> &arr, int difference)
    {
        vector<int> dp(arr.size(), 1);
        unordered_map<int, vector<int>> memo;
        memo[arr[0]].push_back(0);
        int answer = 0;
        for (int i = 1; i < arr.size(); i++)
        {
            for (auto idx : memo[arr[i] - difference])
            {
                // printf("<%d,%d>\n", it->first, it->second);
                dp[i] = max(dp[i], 1 + dp[idx]);
            }
            answer = max(answer, dp[i]);
            memo[arr[i]].push_back(i);
            // printf("%dth max : %d\n", i, dp[i]);
        }

        return answer;
    }
};