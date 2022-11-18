#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int getMoneySpent(const vector<int> &keyboards, const vector<int> &drives, const int &b)
{
    vector<int> vtmp;

    for (int i = 0; i < keyboards.size(); i++)
        for (int j = 0; j < drives.size(); j++)
            if (keyboards.at(i) + drives.at(j) <= b)
                vtmp.push_back(keyboards.at(i) + drives.at(j));

    if (vtmp.size() != 0)
        return *max_element(vtmp.begin(), vtmp.end());

    return -1;
}

int main()
{
    int b, n, m;
    cin >> b >> n >> m;
    vector<int> keyboards(n), drivers(m);

    for (int &val : keyboards)
        cin >> val;

    for (int &val : drivers)
        cin >> val;

    cout << getMoneySpent(keyboards, drivers, b) << '\n';

    return 0;
}