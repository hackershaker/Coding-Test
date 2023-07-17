#include <cstdio>

using namespace std;

int main()
{
    char logo[5][20] = {
        "       _.-;;-._",
        "'-..-'|   ||   |",
        "'-..-'|_.-;;-._|",
        "'-..-'|   ||   |",
        "'-..-'|_.-''-._|",
    };
    for (auto row : logo)
    {
        printf("%s\n", row);
    }
    return 0;
}