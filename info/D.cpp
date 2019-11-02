#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m = 0;
    cin >> n >> m;
    int arr[n][m];
    int dp[n][m];
    vector<char> trail;

    for (int y = 0; y < n; ++y) {
        for (int x = 0; x < m; ++x) {
            cin >> arr[y][x];
            if (y == 0 || x == 0) {
                    if (x == 0) {
                        dp[y][x] = arr[y][x] + dp[y - 1][x];
                    } else {
                        dp[y][x] = arr[y][x] + dp[y][x - 1];
                    }
            } else {
                dp[y][x] = arr[y][x] + max(dp[y - 1][x], dp[y][x - 1]);
            }
        }
    }

    // cout << dp[n - 1][m - 1] << endl;

    int x = m, y = n;
    while (x >= 0 & y >= 0) {
        if (arr[y][x - 1] > arr[y - 1][x]) {
            if (y != 0) {
                cout << 'D';
                y --;
            } else {
                cout << 'R';
                x --;
            }
        } else {
            if (x != 0) {
                cout << 'R';
                x --;
            } else {
                cout << 'D';
                y --;
            }
        }
    }
}
