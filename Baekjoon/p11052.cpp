#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<int> dp(n, 0);
    vector<int> price(n);

    for (int k = 0; k < n; k++)
        cin >> price[k];

    dp[0] = price[0];
    for (int i = 1; i < dp.size(); i++)
    {
        dp[i] = price[i];
        for (int j = 0; j < i; j++)
        {
            dp[i] = max(dp[i], price[j] + dp[i - j - 1]);
        }
    }
    cout << dp[n - 1] << "\n";
    return 0;
}