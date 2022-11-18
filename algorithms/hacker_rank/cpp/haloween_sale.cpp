#include <iostream>
using namespace std;

int howManyGames(int p, int d, int m, int s)
{
    int games = 0;
    int cost = 0;

    while (true)
    {
        cost += p;

        if (cost <= s)
            ++games;
        else
            break;

        if (p - d >= m)
            p -= d;
        else
            p = m;
    }

    return games;
}

int main()
{
    int p, d, m, s;
    cin >> p >> d >> m >> s;
    cout << howManyGames(p, d, m, s) << '\n';
    return 0;
}
