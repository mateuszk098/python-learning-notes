#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;

typedef vector<unsigned short> us_vector;
typedef unsigned short us;

us getTotalX(const us_vector &a, const us_vector &b)
{
    us max_a = *max_element(a.begin(), a.end());
    us min_b = *min_element(b.begin(), b.end());
    // us_vector tmp;
    us counts = 0;

    // One loop version
    for (us val = max_a; val <= min_b; val++)
        if (all_of(a.begin(), a.end(), [val](us j){ return val % j == 0; }))
            if (all_of(b.begin(), b.end(), [val](us j){ return j % val == 0; }))
                counts++;

    // // If val is divisable by all values from vector a (represents by j) then 
    // // add this val to tmp vector
    // for (us val = max_a; val <= min_b; val++)
    //     if (all_of(a.begin(), a.end(), [val](us j){ return val % j == 0; }))
    //         tmp.push_back(val);

    // // If all elements in vector b are divisable by val then count that
    // for (const us &val : tmp)
    //     if (all_of(b.begin(), b.end(), [val](us j){ return j % val == 0; }))
    //         counts++;

    return counts;
}

int main()
{
    us n, m;
    cin >> n >> m;
    us_vector a(n), b(m);

    for (us &val : a)
        cin >> val;

    for (us &val : b)
        cin >> val;

    cout << getTotalX(a, b) << '\n';

    return 0;
}