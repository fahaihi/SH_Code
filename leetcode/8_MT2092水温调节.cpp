#include<bits/stdc++.h>
// 贪心算法

using namespace std;

int main( )
{
    double t1, t2, x1, x2, t0;            // 输入变量
    double y1, y2, t;                     // 过程变量
    double tmax = 0x3f3f3f3f, ans1, ans2; // 结果变量
    cin >> t1 >> t2 >> x1 >> x2 >> t0;
    y1 = x1, y2 = x2;
    while (y1 >=0 && y2 >= 0){
        t = (t1 * y1 + t2 * y2) / (y1 + y2);
        if (t >= t0){
            if (t < tmax)
                tmax = t, ans1 = y1, ans2 = y2;
            y2--;
        }
        else
            y1--;

    }
    cout << ans1 << " " << ans2;
    return 0;
}