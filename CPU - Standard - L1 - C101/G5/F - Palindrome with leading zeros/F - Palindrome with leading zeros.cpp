#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
   
    int n;
    cin >> n;

    string f = to_string(n);
    
    int low = 0;
    int high = f.length() -1;
    
    while (f[low] - '0' == 0) {
        low++;
    }

    while (f[high] - '0' == 0) {
        high--;
    }

    for (int i = low; i <= high; i++) {
        if (f[i] != f[high]) {
            cout << "No" << endl;
            return 0;
        } else {
            high--;
        }
    }

    cout << "Yes" << endl;
    return 0;
}