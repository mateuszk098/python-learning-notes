#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <algorithm>
using namespace std;

typedef unsigned short us;

unsigned utopianTree(const us &n)
{
    unsigned height = 1;

    for (us i = 1; i <= n; i++)
    {
        if (i % 2 != 0)
            height *= 2;
        else
            ++height;
    }

    return height;
}

int main()
{
    us t;
    cin >> t;
    vector<us> vec(t);

    for (us &n : vec)
        cin >> n;

    for (const us &n : vec)
        cout << utopianTree(n) << '\n';

    return 0;
}
