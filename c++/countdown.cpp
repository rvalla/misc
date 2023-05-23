#include <iostream>
#include <stdlib.h>
#include <time.h>

void countDown(int number){
    std::cout << std::to_string(number);
    std::cout << "\n";
    if (number > 0)
        countDown(number - 1);
}

int main() {
    srand(time(NULL));
    int number = rand() % 100;
    countDown(number);
    return 0;
}