#include <iostream>
#include <vector>

#include <cstdint>
 
using namespace std;
int main()
{
    int64_t number_of_icecream_packs, number_of_people_in_line;

    cin >> number_of_people_in_line  >> number_of_icecream_packs;

    int64_t distressed_kids = 0;

    for (int64_t i = 0; i < number_of_people_in_line; i++)
    {
        int64_t amount;
        char op;
        cin >>op  >>  amount;

        if (op == '+')
        {
            number_of_icecream_packs += amount;
        }
        else
        {
            if (number_of_icecream_packs >= amount) {
                number_of_icecream_packs -= amount;
            } else {
                distressed_kids++;
            }


        }
    }

    cout << number_of_icecream_packs << " " <<distressed_kids <<endl;
    
    return 0;
}