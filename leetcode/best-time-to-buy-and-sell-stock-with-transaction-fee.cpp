// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
#include <bits/stdc++.h>
using namespace std;

// 기본적으로 저점에 사서 고점에 산다는 전략을 취하되
// 고점-저점 < fee이면 손해이므로 고점-저점 >= fee일 경우에만 판다
// 그리고 price가 감소했을 때 fee보다 더 크게 감소하면 팔아도 fee보다 더 크게 메꿀 수 있으므로 판다
class Solution
{
public:
    int maxProfit(vector<int> &prices, int fee)
    {
        int buy = 500000, sell = 0, profit = 0;
        for (auto p : prices)
        {
            if (buy >= p)
            {
                if (buy != 0 && sell != 0 && sell - buy > fee)
                {
                    profit += sell - buy - fee;
                }
                buy = p;
                sell = 0;
            }
            else
            {
                if (sell <= p)
                {
                    sell = p;
                }
                else if (sell - p > fee)
                {
                    if (sell - buy > fee)
                    {
                        profit += sell - buy - fee;
                    }
                    buy = p;
                    sell = 0;
                }
            }
        }
        if (buy != 0 && sell != 0 && sell - buy > fee)
            profit += sell - buy - fee;
        return profit;
    }
};