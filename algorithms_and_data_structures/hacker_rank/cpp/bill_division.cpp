#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

void bonAppetit(vector<int> &bill, const int &k, const int &b)
{
    bill.erase(bill.begin() + k);
    int sum = accumulate(bill.begin(), bill.end(), 0);

    if (sum * 0.5 == b)
        cout << "Bon Appetit" << '\n';
    else
        cout << b - sum * 0.5 << '\n';
}

int main()
{
    int n, k, b;
    cin >> n >> k;
    vector<int> bill(n);

    for (int &val : bill)
        cin >> val;

    cin >> b;
    bonAppetit(bill, k, b);

    return 0;
}
