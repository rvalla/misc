#include <iostream>

int main() {
    int number = 0;
    for (int i = 0; i < 5; i++){
        number += 1;
        std::cout << std::to_string(number);
        std::cout << "\n";
    }
    return 0;
}