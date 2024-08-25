#include <iostream>

const int END_LOOP = 1000000000;

int main() {
    int last_number;

    for (int i = 0; i < END_LOOP; i++) {
        last_number = i;
    }
    std::cout << "last_number=" << last_number << std::endl;

    return 0;
}
