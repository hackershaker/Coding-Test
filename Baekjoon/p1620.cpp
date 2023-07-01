#include <unordered_map>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    int n, m;
    unordered_map<string, string> dict;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> s;
        dict.insert({to_string(i), s});
        dict.insert({s, to_string(i)});
    }

    while (m--)
    {
        cin >> s;
        cout << dict[s] << "\n";
    }
    return 0;
}