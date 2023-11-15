#include <iostream>
#include <math.h>
#include <cstdint>

using namespace std;


int main() {

    int64_t n;
    int64_t m;
    int64_t a;


    cin >> n >> m >> a;

    int64_t stones_to_cover_m = (m + a - 1 ) / a;
    int64_t stones_to_cover_n = (n + a - 1 ) / a;
    


    cout << stones_to_cover_n * stones_to_cover_m << endl;


    return 0;
}