#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findMedian(vector<int> v)
{
    int size = v.size();
    if (size == 1)
        return v.back();

    int med = 0;
    sort(v.begin(), v.end());

    if (size % 2 == 0)
        med = (v.at(size / 2) + v.at(size / 2 - 1)) * 0.5;
    else
        med = v.at(size / 2);

    return med;
}

int main()
{
    int N;
    cin >> N;
    vector<int> v(N);

    for (int &val : v)
        cin >> val;

    cout << findMedian(v) << '\n';
    return 0;
}