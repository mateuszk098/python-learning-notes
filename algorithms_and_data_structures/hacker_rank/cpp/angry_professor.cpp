#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

string angryProfessor(const unsigned short &k, const vector<short> v)
{
    unsigned short counts = count_if(v.begin(), v.end(), [](short i){ return i <= 0; });

    if (counts < k)
        return "YES";

    return "NO";
}

int main()
{
    unsigned short cases, n, k;
    cin >> cases;

    for (unsigned short i = 0; i < cases; i++)
    {
        cin >> n >> k;
        vector<short> v(n);
        for (short &val : v)
            cin >> val;

        cout << angryProfessor(k, v) << '\n';
    }

    return 0;
}