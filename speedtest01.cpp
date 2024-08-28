// compile with
// g++ speedtest01.cpp -o speedtest01_cpp.bin

#include <iostream>

#define END_LOOP 1000000000 // 1 Mrd.

int main() {
    unsigned int last_number=0;

    for (unsigned int i = 0; i < END_LOOP; i++) {
        last_number++;
    }
    std::cout << "C++:last_number=" << last_number << "\n--" << std::endl;

    return 0;
}
