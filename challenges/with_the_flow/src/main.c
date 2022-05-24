#include <stdio.h>

void flagged() {
    puts("The flag will be here if you run this function on the server.");
}

int get_quote() {
    char input[128];
    printf(">>> ");
    gets(input);
    return strcasestr(input, "flow") != 0;
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
    setup();

    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ The flow ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("What is your favorite quote that includes the word ~flow~?\n");
    if (get_quote()) {
        printf("While beautiful, you do not seem to have fully given in to the ~flow~.\n");
        return 0;
    } else {
        printf("Not even close ffs. Do you even ~flow~ bro? This ain\'t a free meditation session!\n");
        return 1;
    }
}