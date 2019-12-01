#include <iostream>
#include <fstream>

using namespace std;

const int fuel_req(const int n) {
    return n/3 - 2;
}

const int fuel_req_tot(const int n) {
    int res = fuel_req(n);
    return res <= 0 ? 0 : res + fuel_req_tot(res);
}

int main(int argc, char *argv[]) {
    ifstream infile(argv[1]);
    if (!infile) {
        perror(argv[1]);
        exit(1);
    }

    int total = 0;
    int total2 = 0;
    int n;
    while (infile >> n) {
        total += fuel_req(n);
        total2 += fuel_req_tot(n);
    }

    cout << "part 1: " << total << endl;
    cout << "part 2: " << total2 << endl;
}
