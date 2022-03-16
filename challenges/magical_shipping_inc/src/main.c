#include <stdio.h>

char const* const FLAG = "uhctf{the-best-defense-is-wasting-peoples-time-09bcc8}";

int main () {
    printf("Welcome to Magical Shipping Inc.!\r\n");
    printf("Please provide your package ID: ");

    char package_id[16];
    fgets(package_id, sizeof(package_id), stdin);

    printf("Package not found...\r\n");
    return 0;
}