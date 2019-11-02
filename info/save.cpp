#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long n;
    cin >> n;
    std::vector<char> prime(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            if (!prime[i]) continue;
            for (int j = i*i; j <= n*i; ++i) {
                prime[j] = 0;
            }
        }



    cout << prime(n)
}
