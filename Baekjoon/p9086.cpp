// https://www.acmicpc.net/problem/9086
#include <string>
#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--)
    {
        string s;
        cin >> s;
        cout << s.front() << s.back() << "\n";
    }
    return 0;
}