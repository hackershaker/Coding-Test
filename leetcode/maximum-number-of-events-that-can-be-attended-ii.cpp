#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxValue(vector<vector<int>> &events, int k)
    {
        int i, idx, answer = 0;
        vector<vector<int>> dp(k, vector<int>(events.size(), 0));
        sort(events.begin(), events.end(), comp);
        for (int i = 0; i < events.size(); i++)
        {
            if (i == 0)
                dp[0][i] = events[i][2];
            else
                dp[0][i] = max(dp[0][i - 1], events[i][2]);
            answer = max(answer, dp[0][i]);
        }

        for (int i = 1; i < k; i++)
        {
            for (int j = 0; j < events.size(); j++)
            {
                if (events[j][0] <= events[0][1])
                {
                    dp[i][j] = events[j][2];
                    if (j > 0)
                        dp[i][j] = max(dp[i][j], dp[i][j - 1]);
                }
                else
                {
                    dp[i][j] = dp[i][j - 1];
                    int idx = j - 1;
                    while (idx >= 0)
                    {
                        if (events[idx][1] < events[j][0])
                        {
                            dp[i][j] = max(dp[i][j - 1], events[j][2] + dp[i - 1][idx]);
                            break;
                        }
                        idx -= 1;
                    }
                }
                answer = max(answer, dp[i][j]);
            }
        }

        return answer;
    }

    static bool comp(vector<int> &v1, vector<int> v2)
    {
        return v1[1] < v2[1];
    }
};