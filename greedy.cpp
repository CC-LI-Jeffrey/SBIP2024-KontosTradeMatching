#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

long long mt;
int n;
int c[20];
long long v[20][15];
pair<long long, long long> z1[20];
long long z2[20];
int used[20];

int main()
{
    cin >> mt >> n;
    for (int i = 0; i < n; i++) {
        cin  >> c[i] >> z1[i].first >> z2[i];
        z1[i].second = i;
        for (int j = 0; j < c[i]; j++) {
            cin >> v[i][j];
        }
    }

    sort(z1, z1+n);

    long long m = 0;
    long long cost = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < c[z1[i].second]; j++) {
            cout << z1[i].second << " " << v[z1[i].second][j] << endl;
            m += v[z1[i].second][j] - z2[z1[i].second];
            cost += z2[z1[i].second];
            if (!used[i]) {
                used[i]++;
                m -= z1[i].first;
                cost += z1[i].first;
            }
            if (m >= mt)
                break;
        }
        if (m >= mt)
                break;
    }

    if (m < mt) {
        cout << "No solution" << endl;
        exit(0);
    }

    cout << cost + mt << endl;

    return 0;
}
