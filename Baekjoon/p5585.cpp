// https://www.acmicpc.net/problem/5585
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    vector<int> coin = {500, 100, 50, 10, 5, 1};
    int answer = 0, price;
    scanf("%d", &price);
    price = 1000 - price;

    for (auto c : coin)
    {
        answer += price / c;
        price %= c;
    }

    printf("%d\n", answer);
}