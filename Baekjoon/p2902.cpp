// https://www.acmicpc.net/problem/2902
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    char memo[100];
    string answer;
    scanf("%s", memo);
    bool flag = true;
    for (auto c : memo)
    {
        if (flag)
        {
            answer += c;
            flag = false;
        }
        if (c == '-')
        {
            flag = true;
        }
    }
    cout << answer << endl;
}