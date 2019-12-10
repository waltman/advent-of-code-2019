#include <stdio.h>
#include <iostream>
#include <fstream>
#include "array2d.h"
#include "array3d.h"

using namespace std;

const int ROWS = 6;
const int COLS = 25;
const int STRIDE = ROWS * COLS;

int main(int argc, char *argv[]) {
    ifstream infile(argv[1]);
    if (!infile) {
        perror(argv[1]);
        exit(1);
    }

    char s[20000];
    infile >> s;

    int best_count = 1e6;
    int best_layer = -1;
    for (int z = 0; z < (int) strlen(s); z += STRIDE) {
        int count = 0;
        for (int i = z; i < z+STRIDE; i++)
            if (s[i] == '0')
                count++;
        if (count < best_count) {
            best_count = count;
            best_layer = z;
        }
    }
    int count1 = 0;
    int count2 = 0;
    for (int i = best_layer; i < best_layer + STRIDE; i++) {
        if (s[i] == '1')
            count1++;
        else if (s[i] == '2')
            count2++;
    }    
    cout << "Part 1: " << count1 * count2 << endl;

    const int LAYERS = strlen(s) / ROWS / COLS;
    array3d<int> stack(LAYERS, ROWS, COLS);
    int i = 0;
    for (int z = 0; z < LAYERS; z++)
        for (int r = 0; r < ROWS; r++)
            for (int c = 0; c < COLS; c++)
                stack(z, r, c) = s[i++] - '0';

    array2d<int> output(ROWS, COLS, -1);
    for (int z = 0; z < LAYERS; z++)
        for (int r = 0; r < ROWS; r++)
            for (int c = 0; c < COLS; c++) {
                if (output(r,c) == -1 && stack(z,r,c) != 2)
                    output(r,c) = stack(z,r,c);
            }

    cout << "Part 2:" << endl;
    cout << output << endl;

    char out[20000];
    i = 0;
    for (int r = 0; r < ROWS; r++) {
        for (int c = 0; c < COLS; c++)
            out[i++] = output(r,c) == 0 ? ' ' : '*';
        out[i++] = '\n';
    }
    out[i++] = '\0';
    cout << out;
}
