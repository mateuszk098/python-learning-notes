#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef unsigned short us;

us hurdleRace(const us &k, const vector<us> &height)
{
    us hmax = *max_element(height.begin(), height.end());
    if (k > hmax)
        return 0;
    return hmax - k;
}

int main()
{
    us n, k;
    cin >> n >> k;
    vector<us> height(n);

    for (us &h : height)
        cin >> h;

    cout << hurdleRace(k, height) << '\n';

    return 0;
}