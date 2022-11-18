#include <iostream>
#include <vector>
using namespace std;

vector<int> compareTriplets(const vector<int> &a, const vector<int> &b)
{
    int alice = 0, bob = 0;

    for (int i = 0; i < a.size(); i++)
    {
        if (a.at(i) > b.at(i))
            alice++;
        else if (a.at(i) < b.at(i))
            bob++;
    }

    vector<int> v;
    v.push_back(alice);
    v.push_back(bob);

    return v;
}

int main()
{
    vector<int> a, b;
    int tmp;

    for (int i = 0; i < 3; i++)
    {
        cin >> tmp;
        a.push_back(tmp);
    }

    for (int i = 0; i < 3; i++)
    {
        cin >> tmp;
        b.push_back(tmp);
    }

    vector<int> result;
    result = compareTriplets(a, b);
    for (const auto &val : result)
        cout << val << ' ';

    return 0;
}