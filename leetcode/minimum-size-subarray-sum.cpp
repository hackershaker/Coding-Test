#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int start = 0, end = 0, answer = 0, sum = nums[0];
        while (end < nums.size())
        {
            if (sum < target)
            {
                end++;
                if (end == nums.size())
                    break;
                sum += nums[end];
            }
            else
            {
                answer = (answer == 0) ? (end - start + 1) : min(end - start + 1, answer);
                sum -= nums[start];
                start++;
            }
        }
        return answer;
    }
};