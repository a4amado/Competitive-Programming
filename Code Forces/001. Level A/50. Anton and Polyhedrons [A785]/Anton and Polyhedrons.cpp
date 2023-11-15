#include <iostream>
#include <string>

using namespace std;

int main()
{
    string Tetrahedron = "Tetrahedron"; // 4
    string Cube = "Cube"; // 6
    string Octahedron = "Octahedron"; // 8
    string Dodecahedron = "Dodecahedron"; // 12
    string Icosahedron = "Icosahedron"; // 20

    int n;
    cin >> n;

    int total = 0;

    while ( n >= 0) {
        string s = "";

        getline(cin, s);
        if (s == Tetrahedron) {
            total += 4;
        } else if (Cube == s) {
            total += 6;
        } else if (Octahedron == s) {
            total += 8;
        } else if(s == Dodecahedron) {
            total += 12;
        } else if (s == Icosahedron) {
            total += 20;
        }

        n--;
    }

    cout << total << endl;
    return 0;
}