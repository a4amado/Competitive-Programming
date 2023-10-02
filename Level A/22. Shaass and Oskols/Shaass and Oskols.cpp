#include <iostream>

using namespace std;

int main() {
    int number_of_wires = 0;
    cin >> number_of_wires;

    int *number_of_birds_on_each_line = new int[number_of_wires];
    for (int i = 0; i < number_of_wires; i++) {
        cin >> number_of_birds_on_each_line[i];
    }

    int number_of_birds_to_shoot = 0;
    cin >> number_of_birds_to_shoot;

    int *wires_numbers = new int[number_of_birds_to_shoot];
    int *bird_to_shoot = new int[number_of_birds_to_shoot];

    for (int i = 0; i < number_of_birds_to_shoot; i++) {
        cin >> wires_numbers[i] >> bird_to_shoot[i];
    }

    for (int i = 0; i < number_of_birds_to_shoot; i++) {
        int wire_index = wires_numbers[i] - 1;  // Adjust for 0-based indexing
        int number_of_bird_to_shoot = bird_to_shoot[i];
        int number_of_the_bird_on_the_wire = number_of_birds_on_each_line[wire_index];

        bool is_there_a_wire_above = wire_index != 0;  // Changed 1 to 0
        bool is_there_a_wire_below = wire_index != number_of_wires - 1;  // Adjusted for last wire

        int number_of_birds_to_the_right = number_of_the_bird_on_the_wire - number_of_bird_to_shoot;
        int number_of_birds_to_the_left = number_of_bird_to_shoot - 1;

        if (is_there_a_wire_above) {
            number_of_birds_on_each_line[wire_index - 1] += number_of_birds_to_the_left;
        }
        if (is_there_a_wire_below) {
            number_of_birds_on_each_line[wire_index + 1] += number_of_birds_to_the_right;
        }

        number_of_birds_on_each_line[wire_index] = 0;
    }

    for (int i = 0; i < number_of_wires; i++) {
        cout << number_of_birds_on_each_line[i] << endl;
    }

    delete[] number_of_birds_on_each_line;
    delete[] wires_numbers;
    delete[] bird_to_shoot;

    return 0;
}
