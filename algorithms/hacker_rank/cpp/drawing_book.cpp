#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

unsigned pageCount(const unsigned &n, const unsigned &p)
{
    if (p == 1 || n == p)
        return 0;
    if (n % 2 == 0 && (p == n - 1 || p == n - 2))
        return 1;
    if (n % 2 != 0 && p == n - 1)
        return 0;

    unsigned result = 0;        // minimalna liczba skokow
    unsigned max_jumps = n / 2; // Maksymalna liczba skokow poczynajac od 1 strony
    vector<unsigned> pages(n);
    iota(pages.begin(), pages.end(), 1); // wypelnienie wektora kolejnymi liczbami poczynajac od 1 do n

    ++result; // skok na strony 2, 3 ze strony 1
    // Poczynajac od 2 strony zliczamy ile mamy skokow
    // Skacz co i = 2
    for (unsigned i = 1; i < pages.size() - 1; i += 2)
    {
        // Jezeli strona i lub i+1 zgadza sie z p
        if (p == pages.at(i) || p == pages.at(i + 1))
            break;
        // Jezeli nie to dodaj skok
        ++result;
    }

    // Jezeli szukana strona jest dalej niz za n/2
    if (p > n / 2)
        result = max_jumps - result;

    return result;
}

int main()
{
    unsigned n, p;
    cin >> n >> p;
    cout << pageCount(n, p) << '\n';
    return 0;
}
