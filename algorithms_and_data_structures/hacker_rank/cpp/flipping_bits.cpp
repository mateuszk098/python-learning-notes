#include <iostream>
using namespace std;

unsigned int flippingBits(unsigned int n)
{
    return ~n;
}

int main()
{
    int q;
    unsigned int n;
    cin >> q;

    while (q--)
    {
        cin >> n;
        cout << flippingBits(n) << endl;
    }

    return 0;
}