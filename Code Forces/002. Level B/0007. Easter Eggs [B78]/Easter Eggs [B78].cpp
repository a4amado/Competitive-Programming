// #include <iostream>
// #include <vector>
// #include <string>
// #include <cmath>

// using namespace std;

// int main()
// {
//     vector<string> colors = {"R", "O", "Y", "G", "B", "I", "V"};
//     int n;
//     cin >> n;

//     if (n % 7 == 0)
//     {
//         for (int i = 0; i < n; i++)
//         {
//             cout << colors.at(i % 7);
//         }
//         cout << endl;
//         return 0;
//     }
//     int reminder = n % 7;


//     for (int i = 0; i <= n - reminder; i++)
//     {
//         cout << colors[i];
//     }


//     if (reminder >= 4)
//     {
//         for (int i = 0; i < reminder; i++)
//         {
//             cout << colors[i];
//         }
//     } else {
//         for (int i = 7 / reminder; i < (7 / reminder) + reminder + 1; i++)
//         {
//             cout << colors[i];
//         }
//     }

//     cout << endl;

//     return 0;
// }