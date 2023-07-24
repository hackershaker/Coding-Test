// https://leetcode.com/problems/powx-n
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double myPow(double x, int n)
    {
        if (n == 0)
            return 1.0;
        if (n == 1)
            return x;
        if (n == -1)
            return 1 / x;
        if (n % 2 == 0)
        {
            auto result = myPow(x, n / 2);
            return result * result;
        }
        else
        {
            auto result = myPow(x, n / 2);
            return result * result * myPow(x, n % 2);
        }
    }
};