#include <bits/stdc++.h>
using namespace std;

long long mt;
int n;
int c[20];
long long v[20][15];
long long z1[20];
long long z2[20];
long long f[20][10000];
long long g[21][10000];
const long long INF = 1e18;

int main()
{
    cin >> mt >> n;
    for (int i = 0; i < n; i++) {
        cin >> c[i] >> z1[i] >> z2[i];
        for (int j = 0; j < c[i]; j++) {
            cin >> v[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        sort(v[i], v[i]+c[i], greater<long long>());
        for (int j = 1; j < 10000; j++) {
            long long est = -z1[i];
            int qty = 0;
            for (int k = 0; k < c[i]; k++) {
                est = est + v[i][k] - z2[i];
                qty++;
                if (est >= j) {
                    break;
                }
            }
            if (est >= j) {
                f[i][j] = qty * z2[i] + z1[i];
            }
            else {
                f[i][j] = INF;
            }
        }
    }

    for (int j = 1; j < 10000; j++)
        g[0][j] = INF;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < 10000; j++) {
            long long minV = INF;
            for (int k = 0; k <= j; k++) {
                minV = min(f[i-1][k] + g[i-1][j-k], minV);
            }
            g[i][j] = minV;
        }
    }
    if (g[n][mt] != INF) {
        cout << g[n][mt] + mt << endl;
    }
    else {
        cout << "No solution" << endl;
    }

    return 0;
}
