#include <iostream>
#include <vector>
using namespace std;
typedef unsigned short us;

us jumpingOnClouds(const vector<us> &c)
{

    us jumps = 0;
    us s = c.size();

    for (us i = 0; i < s; i++)
    {
        // Wykonaj skok o 1 miejsce miedzy chmurami
        jumps++;
        // Jezeli jeszcze jest miejsce oraz dwie chmury sa zwykle to skocz o 2 miejsca
        if (i < s - 2 && c.at(i + 2) == 0)
            i++;
    }

    return jumps - 1;
}

int main()
{
    us n;
    cin >> n;
    vector<us> clouds(n);

    for (us &val : clouds)
        cin >> val;

    cout << jumpingOnClouds(clouds) << '\n';
}