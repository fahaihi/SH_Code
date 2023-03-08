#include<bits/stdc++.h>
#include <vector>
using namespace std;

int main( )
{

    int n;
    cin >> n;
    vector<int>a(n+2);
    //int a[n];
    for(int i=0; i<n; i++) cin >> a[i];
    int ans = 0;
    while(n>=3){
        ans++;
        for(int i=0; i<n-2; i++){
            int sum = a[i] + a[i+1] + a[i+2];
            if(sum <= ans*3){
                a[i] = sum;
                for(int j=i+1; j<n; j++) a[j]=a[j+2];
                n=n-2;
            }
        }
    }
    cout << ans << endl;
    return ans;
}