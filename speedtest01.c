// compile with:
// gcc speedtest01.c -o speedtest01_c.bin

#include <stdio.h>

const unsigned int END_LOOP = 1000000000;

void main() {
    unsigned int last_number;

    for (unsigned int i = 0; i < END_LOOP; i++) {
        last_number = i;
    }
    printf("last_number=%d\n", last_number);
}
