#include <iostream>
#include <vector>
#include <numeric>
#include <map>
using namespace std;

typedef unsigned short us;

us pickingNumbers(const vector<us> &v)
{
    // Zlicz ile mamy danych liczb, kluczem jest liczba, wartoscia jest ilosc tych liczb
    map<us, us> map_counts;
    for (const us &val : v)
        ++map_counts[val];

    // Szukanie maximum wartosci w mapie
    us max_val = 0;
    for (const auto &[key, value] : map_counts)
        if (value > max_val)
            max_val = value;

    // Zlicz wartosci tylko takich par ktore sasiaduja ze soba kluczami tzn 2,3 albo 5,6 itd.
    us last_value = 0, last_key = map_counts.begin()->first, max = max_val;
    for (const auto &[key, value] : map_counts)
    {
        if ((last_value + value) > max && (key - last_key) == 1)
            max = last_value + value;

        last_value = value;
        last_key = key;
    }

    // Wyswietlanie mapy
    // for (const auto &[key, value] : map_counts)
    // {
    //     cout << "[" << key << "] = " << value << ' ';
    // }
    // cout << '\n';

    return max;
}

int main()
{
    us n;
    cin >> n;

    vector<us> v(n);
    for (us &val : v)
        cin >> val;

    cout << pickingNumbers(v) << '\n';
    return 0;
}
