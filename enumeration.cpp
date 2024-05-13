#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

long long mt;
int n;
int oc[20];
int c[20];
int cn1;
long long ov[20][15];
long long v[20][15];
long long oz1[20];
long long z1[20];
pair<long long, int> oz2[20];
long long z2[20];
vector<pair<long long, long long>> a;
vector<pair<long long, long long>> b;
vector<int> prefixMinCostIdx;
long long value = 0;
long long cost = 0;
long long minCost = INF;
long long nextVal = 0;

void enumerate(int i, int i2)
{
    if (value >= mt) {
        if (cost < minCost)
            minCost = cost;
        return;
    }
    if (i == i2) {
        if (i2 == cn1) {
            a.push_back({value, cost});
        }
        else {
            b.push_back({value, cost});
        }
        return;
    }

    for (int j = 0; j <= c[i]; j++) {
        if (j > 0) {
            if (v[i][j-1] <= nextVal) {
                return;
            }
        }
        for (int k = 0; k < j; k++) {
            value += v[i][k] - z2[i];
            cost += z2[i];
        }
        if (j) {
            value -= z1[i];
            cost += z1[i];
        }

        if (j < c[i] -1)
            nextVal = v[i][j];

        enumerate(i+1, i2);

        nextVal = 0;

        for (int k = 0; k < j; k++) {
            value -= v[i][k] - z2[i];
            cost -= z2[i];
        }
        if (j) {
            value += z1[i];
            cost -= z1[i];
        }
    }

}

int binarySearch(int low, int high, int i)
{
    int idx = -1;
    while (low <= high) {
        int mid = (high + low) / 2;
        if (b[mid].first >= mt - a[i].first) {
            low = mid + 1;
            idx = mid;
        }
        else {
            high = mid - 1;
        }
    }
    return idx;
}

int main()
{
    cin >> mt >> n;
    for (int i = 0; i < n; i++) {
        cin >> oc[i] >> oz1[i] >> oz2[i].first;
        oz2[i].second = i;
        for (int j = 0; j < oc[i]; j++) {
            cin >> ov[i][j];
        }
    }
    sort(oz2, oz2 + n);
    for (int i = 0; i < n; i++) {
        c[i] = oc[oz2[i].second];
        z1[i] = oz1[oz2[i].second];
        z2[i] = oz2[i].first;
        for (int j = 0; j < c[i]; j++) {
            v[i][j] = ov[oz2[i].second][j];
        }
    }
    for (int i = 0; i < n; i++) {
        sort(v[i], v[i]+c[i], greater<long long>());
    }

    cn1 = (n%2 == 0 ? n/2 : n/2+1);
    enumerate(0, cn1);
    enumerate(cn1, n);

    sort(b.rbegin(),b.rend());
    prefixMinCostIdx.push_back(0);
    for (int i = 1; i < b.size(); i++) {
        if (b[prefixMinCostIdx[i-1]].second > b[i].second)
            prefixMinCostIdx.push_back(i);
        else
            prefixMinCostIdx.push_back(prefixMinCostIdx[i-1]);
    }

    for (int i = 0; i < a.size(); i++) {
        int lastIdx = binarySearch(0, b.size() - 1, i);
        if (lastIdx != -1) {
            if (minCost > a[i].second + b[prefixMinCostIdx[lastIdx]].second && a[i].first + b[prefixMinCostIdx[lastIdx]].first >= mt)
                minCost = a[i].second + b[prefixMinCostIdx[lastIdx]].second;
        }
    }

    if (minCost != INF)
        cout << minCost+mt << endl;
    else
        cout << "No solution" << endl;

    return 0;
}

