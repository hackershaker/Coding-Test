// https://leetcode.com/problems/asteroid-collision/description/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> asteroidCollision(vector<int> &asteroids)
    {
        vector<int> stack;
        for (auto asteroid : asteroids)
        {
            if (stack.empty() || (stack.back() * asteroid > 0) || (stack.back() < 0 && asteroid > 0))
            {
                stack.push_back(asteroid);
                continue;
            }
            bool isAsteroidExplode = false;
            while (!stack.empty() && stack.back() > 0 && asteroid < 0)
            {
                if (asteroid * -1 == stack.back())
                {
                    stack.pop_back();
                    isAsteroidExplode = true;
                    break;
                }
                else if (asteroid * -1 < stack.back())
                {
                    isAsteroidExplode = true;
                    break;
                }
                else
                    stack.pop_back();
            }

            if (!isAsteroidExplode)
                stack.push_back(asteroid);
        }
        return stack;
    }
};