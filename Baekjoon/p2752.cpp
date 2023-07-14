// https://www.acmicpc.net/problem/2752
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> nums;
    for (int i = 0; i < 3; i++)
    {
        int num;
        scanf("%d", &num);
        nums.push_back(move(num));
    }

    sort(nums.begin(), nums.end());
    for (auto n : nums)
        printf("%d ", n);

    return 0;
}