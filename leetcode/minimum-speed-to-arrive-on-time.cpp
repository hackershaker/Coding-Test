// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int minSpeedOnTime(vector<int> &dist, double hour)
    {
        int start = 1, end = 10000001;
        double mid;
        while (start < end)
        {
            mid = (start + end) / 2;
            double time = 0.0;
            for (int i = 0; i < dist.size(); i++)
            {
                if (i == dist.size() - 1)
                    time += dist[i] / mid;
                else
                    time += ceil(dist[i] / mid);
            }
            if (time > hour)
                start = mid + 1;
            else
                end = mid;
        }
        if (start == 10000001)
            return -1;
        return end;
    }
};