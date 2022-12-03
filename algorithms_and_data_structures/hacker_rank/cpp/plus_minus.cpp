#include <iostream>
#include <vector>
#include <iomanip> // setprecision
using namespace std;

void plusMinus(const vector<int> &v)
{
    unsigned short pos = 0, neg = 0, zero = 0;
    unsigned short size = v.size();

    for (int i = 0; i < size; i++)
    {
        if (v.at(i) > 0)
            pos++;
        else if (v.at(i) < 0)
            neg++;
        else
            zero++;
    }

    cout << pos / (double)size << '\n';
    cout << neg / (double)size << '\n';
    cout << zero / (double)size << '\n';
}

int main()
{
    vector<int> v;
    int n, tmp;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
    }

    cout << fixed << setprecision(6);
    plusMinus(v);

    return 0;
}