// MT2036 移水造海
#include<bits/stdc++.h>

using namespace std;

int main( )
{
    int ans = 0;
    int max_num = 0;
    int n;
    cin >> n;
    int a[n];
    for(int i=0; i<n; i++){
        cin >> a[i];
        if(a[i] >= max_num) max_num = a[i];
    }

    for(int i=1; i<=max_num; i++){ // 扫描层数
        int last = -1;             // 左侧开始标志
        for(int j=0; j<n; j++){    // 扫描列数
            if(a[j]>i){            // 当前扫描的列要比当前层数大，且位于左侧
                if(last != -1)     // 找到了左侧，且在右侧找到的比左侧大
                    ans = ans + j - last -1;    // j-last-1 是此刻能够容纳水的数目
                last = j;          // 更新边界
            }
        }
    }
    cout << ans;
    return 0;
}