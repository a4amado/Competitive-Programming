#include <iostream>
#include <cmath>

long long binomialCoefficient(int n, int k) {
    if (k == 0 || k == n) {
        return 1;
    }
    if (k > n - k) {
        k = n - k;
    }

    long long result = 1;
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }

    return result;
}

long long maximumValueInTable(int n) {
    return binomialCoefficient(2 * n - 2, n - 1);
}

int main() {
    int n;
    std::cin >> n;

    std::cout << maximumValueInTable(n) << std::endl;

    return 0;
}
