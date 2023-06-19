// https://leetcode.com/problems/find-the-highest-altitude/
#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int largestAltitude(vector<int> &gain)
    {
        int answer = 0, points = 0;
        for (auto height : gain)
        {
            points += height;
            answer = max(answer, points);
        }
        return answer;
    }
};