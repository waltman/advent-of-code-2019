#include <stdio.h>

const int START = 183564;
const int END   = 657474;
const int LEN   = 6;

bool is_sorted(const char *s) {
    for (int i = 0; i < LEN-1; i++)
        if (s[i] > s[i+1])
            return false;
    return true;
}

int main(int argc, char *argv[]) {
    int n1 = 0;
    for (int i = START; i <= END; i++) {
        char s[LEN+1];
        sprintf(s, "%d", i);
        if (is_sorted(s)) {
            for (int j = 0; j < LEN-1; j++) {
                if (s[j] == s[j+1]) {
                    n1++;
                    break;
                }
            }
        }
    }
    printf("Part 1 %d\n", n1);

    int n2 = 0;
    for (int i = START; i <= END; i++) {
        char s[LEN+1];
        sprintf(s, "%d", i);
        if (is_sorted(s)) {
            for (int j = 0; j < LEN-1; j++) {
                if (s[j] == s[j+1]) {
                    if (j > 0 && s[j] == s[j-1])
                        continue;
                    else if (j < LEN-2 && s[j] == s[j+2])
                        continue;
                    else {
                        n2++;
                        break;
                    }
                }
            }
        }
    }
    printf("Part 2 %d\n", n2);
}
