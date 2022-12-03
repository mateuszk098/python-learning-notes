#include <iostream>
using namespace std;

int maximizingXor(int l, int r)
{
    int max = l ^ r;

    for (int a = l; a <= r; a++)
    {
        for (int b = l + 1; b <= r - 1; b++)
        {
            int tmp = a ^ b;
            if (tmp > max)
                max = tmp;
        }
    }

    return max;
}

int main()
{
    int l, r;
    cin >> l >> r;
    cout << maximizingXor(l, r);
    return 0;
}