#include <iostream>
#include <vector>
using namespace std;

vector<int> permutationEquation(const vector<int> &p)
{
    vector<int> y;
    int size = p.size();
    int *p_inv = new int[size + 1];

    for (int i = 1; i <= size; i++)
        p_inv[p.at(i - 1)] = i;

    for (int i = 1; i <= size; i++)
        y.push_back(p_inv[p_inv[i]]);

    // for (const int &val : y)
    //     cout << val << ' ';

    delete[] p_inv;

    return y;
}

int main()
{
    int n;
    cin >> n;
    vector<int> p(n);
    for (int &val : p)
        cin >> val;

    vector<int> y{permutationEquation(p)};
    for (const int &val : y)
        cout << val << '\n';

    return 0;
}
