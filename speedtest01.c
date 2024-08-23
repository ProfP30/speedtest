// compile with:
// gcc speedtest01.c -o speedtest01_c.bin

#include <stdio.h>

const int END_LOOP = 1000000000;

void main() {
    int last_number;

    for (int i = 0; i < END_LOOP; i++) {
        last_number = i;
    }
    printf("last_number=%d\n", last_number);
}
