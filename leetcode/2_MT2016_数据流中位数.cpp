// MT2016数据流中位数
// interesting
// 用堆来进行操作，小顶堆和大顶堆 priority_queue
// 奇数放在大顶堆
#include<bits/stdc++.h>
using namespace std;
const int N = 100000;
priority_queue<int, vector<int>, less<int>> q1;     // 大顶堆，存储小一半的数
priority_queue<int, vector<int>, greater<int>> q2;  // 小顶堆，存储大的一半
void insert(int num){
    if(q1.size() > q2.size()){
        // 放入前多一个，放入后两个堆相等
        q1.push(num);
        q2.push(q1.top());
        q1.pop();
    }
    else{
        // 放入前两个堆数目相等
        q1.push(num); // 放入q1，看是否需要交换堆头
        if(q2.size()!=0 && q1.top()>q2.top()){ // 执行交换
            q2.push(q1.top()); q1.pop();
            q1.push(q2.top()); q2.pop();
        }
    }
}


int main( )
{
    int n, num;
    cin >> n;
    while(n--){
        char ch;
        cin >> ch;
        if(ch=='+'){
            cin >> num;
            insert(num);
        }
        else{
            if(q1.size() > q2.size()) cout << q1.top() << endl;
            else cout << (float)(q1.top() + q2.top()) / 2 << endl;
        }
    }
    return 0;
}