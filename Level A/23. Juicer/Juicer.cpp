#include <iostream>

using namespace std;

int main()
{

    int number_of_oranges, max_size_of_orange, waste_section_capacity;

    cin >> number_of_oranges >> max_size_of_orange >> waste_section_capacity;

    int num_of_times_to_empty_the_waste_section = 0;

    int current_capacity = 0;
    for (int i = 0; i < number_of_oranges; i++)
    {

        int current_orange_size;
        cin >> current_orange_size;

        if (current_orange_size > max_size_of_orange)
        {
            continue;
        }

        current_capacity += current_orange_size;

        if (current_capacity > waste_section_capacity)
        {
            current_capacity = 0;
            num_of_times_to_empty_the_waste_section++;
        };
    }
    cout << num_of_times_to_empty_the_waste_section << endl;
    return 0;
};