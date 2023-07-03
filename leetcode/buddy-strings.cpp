// https://leetcode.com/problems/buddy-strings/
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool buddyStrings(string s, string goal)
    {
        if (s.size() != goal.size())
            return false;
        vector<pair<int, int>> diff;
        vector<int> sarr(26, 0), goalarr(26, 0);
        for (int i = 0; i < s.size(); i++)
        {
            sarr[s[i] - 'a']++;
            goalarr[goal[i] - 'a']++;

            if (s[i] != goal[i])
            {
                diff.push_back(make_pair(s[i], goal[i]));
            }
        }

        if (diff.size() == 0)
        {
            for (auto k : sarr)
            {
                if (k > 1)
                    return true;
            }
        }
        else if (diff.size() == 2)
        {
            auto d1 = diff[0];
            auto d2 = diff[1];
            if (d1.first == d2.second && d2.first == d1.second)
                return true;
        }

        return false;
    }
};