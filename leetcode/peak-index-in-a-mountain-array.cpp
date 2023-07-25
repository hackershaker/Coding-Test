// https://leetcode.com/problems/peak-index-in-a-mountain-array/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int peakIndexInMountainArray(vector<int> &arr)
    {
        int start = 0, end = arr.size() - 1, mid;
        while (start < end)
        {
            // printf("%d,%d\n", start, end);
            mid = (start + end) / 2;
            if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1])
            {
                return mid;
            }
            else if (arr[mid] < arr[mid + 1])
            {
                start = mid;
            }
            else
            {
                end = mid;
            }
        }
        return mid;
    }
};