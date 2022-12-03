#include <iostream>
#include <vector>
#include <map>
using namespace std;

int migratoryBirds(const vector<int> &v)
{
    map<int, int> pairs;
    int map_value = 0, map_key = -1;

    // Przechodzi przez elementy wektora v i uzupelnia mape, ktorej kluczami sa elementy wektora
    // v a wartosciami sa zliczenia tych elementow, mapa jest posortowana i wystepuja w niej tylko
    // unikalne klucze, wiec nie ma powtorek
    for (const int &value : v)
        ++pairs[value];

    // Szukanie maximum wartosci w mapie
    for (const auto &[key, value] : pairs)
    {
        if (value > map_value)
        {
            map_key = key;
            map_value = value;
        }
    }

    // Odpowiedzia jest klucz, ktory odpowiada najwiekszej wartosci w mapie
    return map_key;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);

    for (int &val : v)
        cin >> val;

    cout << migratoryBirds(v) << '\n';

    return 0;
}
