#include <stdio.h>
#include "file-exporter.h"

extern int x, y, z;
int uninitialised;

int main(int argc, char *argv[]) {
    
    initializeResourcePack();
    printf("x=%d, y=%d, z=%d, un=%d\n", x, y, z, uninitialised);
    return 0;
}

