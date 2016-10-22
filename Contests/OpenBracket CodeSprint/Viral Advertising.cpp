#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int next_day(int users) {
    users /= 2;
    users *= 3;
    return users;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;

    int total = 0, current_user = 5;
    for (int day = 1; day <= n; ++day) {
        total += current_user / 2;
        current_user = (current_user / 2) * 3;
    }

    cout << total;
    return 0;
}
