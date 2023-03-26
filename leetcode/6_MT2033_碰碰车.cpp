// MT2033 碰碰车
// 不管有多少车，车的相对位置永远不变
#include<bits/stdc++.h>

using namespace std;

struct CAR {
    int ID;  // 车辆输入ID
    int x;   // 位置
    int f;   // 方向
} car[1010];

bool cmp1(CAR a, CAR b) { return a.x <= b.x; }
bool cmp2(CAR a, CAR b) { return a.ID <= b.ID; }

int n, t, tmp[1010];

int main( )
{
    cin >> n >> t;
    for(int i=0; i<n; i++){
        cin >> car[i].x >> car[i].f;
        car[i].ID = i + 1;
    }
    sort(car, car+n, cmp1);
    for(int i=0; i<n; i++){
        tmp[i] = car[i].ID;
        car[i].x = car[i].x + car[i].f * t;
    }
    sort(car, car+n, cmp1);
    for(int i=0; i<n ; i++){
        car[i].ID = tmp[i];
        if(i<n-1 && car[i].x==car[i+1].x || i>0 && car[i].x == car[i-1].x)
            car[i].f = 0;
    }
    sort(car, car+n, cmp2);
    for(int i=0; i<n; i++, puts("")){
        cout << car[i].x << car[i].f;
    }

    return 0;
}