// https://leetcode.com/problems/longest-arithmetic-subsequence/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestArithSeqLength(vector<int> &nums)
    {
        int answer = 2;
        vector<unordered_map<int, int>> dp(nums.size());
        for (int i = 1; i < nums.size(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                int diff = nums[i] - nums[j];
                if (dp[j].find(diff) != dp[j].end())
                {
                    if (dp[j][diff] + 1 > dp[i][diff])
                    {
                        dp[i][diff] = dp[j][diff] + 1;
                        answer = max(answer, dp[i][diff]);
                    }
                }
                else
                    dp[i].insert(make_pair(diff, 2));
            }
            for (auto key : dp[i])
            {
                printf("<%d : %d>", key.first, key.second);
            }
            printf("\n============\n");
        }
        return answer;
    }
};