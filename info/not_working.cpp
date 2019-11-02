#include <iostream>
using namespace std;

int gcd(int x, int y) {
    while (y) {
        x %= y;
        swap(x, y);
    }
    return x;
}

int main() {
    int n, maxx = -1, max_a, max_b, b, g = 0;
    cin >> n;

    if (n % 2 == 0) {
        cout << n / 2 << ' ' << n / 2;

    } else {
        for (int a = 1; a * a <= n; ++a) {
            b = n - a;
            g = gcd(a, b);
            if (g >= maxx) {
                maxx = g;
                max_a = a;
                max_b = b;
            }
        }
        cout << max_a << ' ' << max_b;
    }
}
