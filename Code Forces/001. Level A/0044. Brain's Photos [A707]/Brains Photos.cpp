#include <iostream>
using namespace std;

char cayan = 'C';
char magenta = 'M';
char yellow = 'Y';

char white = 'W';
char grey = 'G';
char black = 'B';

int main()
{
    int num_of_pictures, number_pixels;
    cin >> num_of_pictures >> number_pixels;

    for (int i = 0; i < num_of_pictures; i++)
    {
        for (int j = 0; j < number_pixels; j++)
        {
            char d;
            cin >> d;

            if (d == cayan || d == magenta || d == yellow)
            {
                cout << "#Color" << endl;
                return 0;
            }
        }
    }
    cout << "#Black&White" << endl;
    return 0;
}