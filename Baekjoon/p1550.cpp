// https://www.acmicpc.net/problem/1550
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;

int hextoInt(string str)
{
    int result = 0;
    for (int i = 0; i < str.size(); i++)
    {
        if (65 <= str[i] && str[i] <= 70)
        {
            result += (str[i] - 55) * pow(16, str.size() - i - 1);
        }
        else
        {
            result += (str[i] - 48) * pow(16, str.size() - i - 1);
        }
    }
    return result;
}

int main()
{
    char num[7] = {0};
    int answer = 0;
    string s;
    scanf("%s", num);
    for (auto ch : num)
    {
        if (ch != 0 && ch != '\0')
            s += ch;
    }
    printf("%d", hextoInt(s));
}