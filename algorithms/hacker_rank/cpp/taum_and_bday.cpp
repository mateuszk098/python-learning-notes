#include <iostream>
using namespace std;

long taumBday(const long &b, const long &w, const long &bc, const long &wc, const long &z)
{
    long all = b * bc + w * wc;
    long b_to_w = b * (wc + z);
    long w_to_b = w * (bc + z);

    if (b_to_w + w * wc < all)
        return b_to_w + w * wc;
    else if (w_to_b + b * bc < all)
        return w_to_b + b * bc;

    return all;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int b, w;
        cin >> b >> w;
        int bc, wc, z;
        cin >> bc >> wc >> z;
        cout << taumBday(b, w, bc, wc, z) << '\n';
    }

    return 0;
}
