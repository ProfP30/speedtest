// compile with
// g++ speedtest01.cpp -o speedtest01_cpp.bin

#include <iostream>

const unsigned int END_LOOP = 1000000000;

int main() {
    unsigned int last_number;

    for (unsigned int i = 0; i < END_LOOP; i++) {
        last_number = i;
    }
    std::cout << "last_number=" << last_number << std::endl;

    return 0;
}
