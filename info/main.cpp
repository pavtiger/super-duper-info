#include <iostream>
using namespace std;

int main(){
    int sum1, sum2;
    int a0, b0, a1, b1, a2, b2, a3, b3;
    cin >> a0 >> b0;
    cin >> a1 >> b1;
    cin >> a2 >> b2;
    cin >> a3 >> b3;
    sum1 = a0 + a1 + a2 + a3;
    sum2 = b0 + b1 + b2 + b3;
    if (sum1 == sum2) {
        cout << "DRAW";
    }
    else {
        if (sum1 > sum2) {
            cout << "1";
        }
        else {
            cout << "2";
        }
    }
}
