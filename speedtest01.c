// compile with:
// gcc speedtest01.c -o speedtest01_c.bin

#include <stdio.h>

#define END_LOOP 1000000000 // 1 Mrd.

void main() {
    unsigned int last_number=0;

    for (unsigned int i = 0; i < END_LOOP; i++) {
        last_number++;
    }
    printf("C:last_number=%d\n", last_number );
}
