#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int lonelyinteger(vector<int> a)
{
    if (a.size() == 1)
        return a.front();

    sort(a.begin(), a.end());
    int i = 0;

    while (i < a.size() - 1)
    {
        if (a[i] == a[i + 1])
            i += 2;
        else if (a[i] < a[i + 1])
            return a[i];
        else
            return a[i + 1];
    }

    return a.back();
}

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &v : a)
        cin >> v;

    cout << lonelyinteger(a) << '\n';
    return 0;
}