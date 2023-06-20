// https://leetcode.com/problems/k-radius-subarray-averages/
#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> getAverages(vector<int> &nums, int k)
    {
        vector<int> answer(nums.size(), -1);
        long long int sum = 0;
        int i = 0;
        if (nums.size() < 2 * k + 1)
        {
            return answer;
        }
        for (i = 0; i < k; i++)
        {
            sum += nums[i];
        }
        for (i = 0; i < nums.size(); i++)
        {
            if (i + k < nums.size())
                sum += nums[i + k];
            if (i - k >= 1)
                sum -= nums[i - k - 1];
            if (i - k < 0 || i + k >= nums.size())
            {
                answer[i] = (-1);
            }
            else
            {
                answer[i] = (sum / (1 + 2 * k));
            }
        }

        return answer;
    }
};