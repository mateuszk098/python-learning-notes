#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

void kaprekarNumbers(int p, int q)
{
    vector<int> v;

    for (long long i = p; i <= q; i++)
    {
        if (i == 0)
            cout << i << ' ';
        else if (i == 1)
            cout << i << ' ';
        else if (i == 2)
            ;
        else if (i == 3)
            ;
        else
        {
            long long square = i * i;
            int iSize = trunc(log10(i)) + 1;
            int sqSize = trunc(log10(square)) + 1;

            string str = to_string(square);
            int l = sqSize - iSize;
            int right = stoi(str.substr(l));
            int left = stoi(str.substr(0, l));

            if (right + left == i)
                v.push_back(i);
        }
    }

    if (v.size() == 0)
        cout << "INVALID RANGE" << '\n';
    else
    {
        for (const int &val : v)
            cout << val << ' ';
    }
}

int main()
{
    int p, q;
    cin >> p >> q;
    kaprekarNumbers(p, q);

    return 0;
}