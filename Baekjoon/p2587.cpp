#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    vector<int> nums;
    int i;
    for (i = 0; i < 5; i++)
    {
        int num;
        scanf("%d", &num);
        nums.push_back(move(num));
    }

    sort(nums.begin(), nums.end(), greater());

    int sum = accumulate(nums.begin(), nums.end(), 0);
    printf("%d\n", sum / 5);
    printf("%d\n", nums[2]);
}