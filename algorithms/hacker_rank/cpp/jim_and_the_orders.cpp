#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> jimOrders(vector<vector<int>> orders)
{
    int n = orders.size();

    vector<pair<int, int>> sum(n);
    for (int i = 0; i < n; i++)
    {
        sum[i].first = orders[i][0] + orders[i][1];
        sum[i].second = i + 1;
    }
    sort(sum.begin(), sum.end());

    vector<int> index(n);
    for (int i = 0; i < n; i++)
    {
        index[i] = sum[i].second;
    }

    return index;
}

int main()
{
    int n;
    cin >> n;

    vector<vector<int>> orders(n);
    for (int i = 0; i < n; i++)
    {
        int order, prep;
        cin >> order >> prep;
        orders[i].resize(2);
        orders[i][0] = order;
        orders[i][1] = prep;
    }

    vector<int> index(jimOrders(orders));
    for (const int &value : index)
        cout << value << ' ';

    // for (int i = 0; i < n; i++)
    // {
    //     cout << orders[i][0] << ' ' << orders[i][1] << '\n';
    // }

    return 0;
}