#include <iostream>
#include <string>
using namespace std;

int findDigits(const int &n)
{
    int count = 0;
    string str = to_string(n);
    for (const char &c : str)
    {
        // int digit = (int)c - 48;
        // cout << digit << ' ' << '\n';
        if ((c - 48) != 0 && n % (c - 48) == 0)
            count++;
    }

    return count;
}

int main()
{
    int cases, n;
    cin >> cases;

    for (int i = 0; i < cases; i++)
    {
        cin >> n;
        cout << findDigits(n) << '\n';
    }
}
