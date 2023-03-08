// MT2042 硬币塔
// 要点：递归
#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll coin[54], gold[45];

ll find(ll n, ll i){
    if(i == 0)
        return 0;
    if(n == 0)
        return 1;
    if(1 >=i )
        return 0;
    if(coin[n-1] + 1 >= i)
        return find(n-1, i-1);
    if(coin[n-1] + 1 + n >= i)
        return gold[n-1] + i - (coin[n-1] + 1); // 超出部分之和
    if(2*coin[n-1] + n + 1 >= i)
        return gold[n-1] + n + find(n-1, i - n -coin[n-1] - 1);
    return gold[n];
}

int main( )
{
    ll n, i;
    cin >> n >> i;
    coin[0] = gold[0] = 1;
    for(int k=1; k<=n; k++){
        // 填充数组，保存中间结果
        coin[k] = coin[k-1] * 2 + k +2;
        gold[k] = gold[k-1] *2 + k;
    }
    cout << find(n, i);
    return 0;
}