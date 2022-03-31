#include <stdio.h> // printf & fgets
#include <stdlib.h> // exit
#include <sys/ptrace.h> // should be obvious :)

char const* const FLAG = "uhctf{the-best-defense-is-wasting-peoples-time-09bcc8}";

void install_anti_debug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1)
    {
        printf("Nice try but that won't work! If you're interested how I'm preventing you from doing this though, see https://www.aldeid.com/wiki/Ptrace-anti-debugging ");
        exit(1);
    }
}

int main () {
    install_anti_debug();

    printf("Welcome to Magical Shipping Inc.!\r\n");
    printf("Please provide your package ID: ");

    char package_id[16];
    fgets(package_id, sizeof(package_id), stdin);

    printf("Package not found...\r\n");
    return 0;
}
