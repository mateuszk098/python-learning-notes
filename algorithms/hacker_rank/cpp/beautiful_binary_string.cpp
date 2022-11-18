#include <iostream>
using namespace std;

int beautifulBinaryString(string b)
{
    int counter = 0;
    int i = 1;

    while (i < b.length() - 1)
    {
        if (b[i - 1] == '0' && b[i] == '1' && b[i + 1] == '0')
        {
            b[i + 1] = '1';
            ++counter;
            ++i;
        }
        else
        {
            ++i;
        }
    }

    return counter;
}

int main()
{
    int n;
    cin >> n;
    string b;
    cin >> b;
    cout << beautifulBinaryString(b) << '\n';
    return 0;
}