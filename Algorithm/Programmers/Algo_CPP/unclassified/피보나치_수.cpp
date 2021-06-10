//https://programmers.co.kr/learn/courses/30/lessons/12945
//피보나치 수
#include<iostream>

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int f1 = 0,f2 = 1, f3=0;
    int div = 1234567;
    for (int i = 0; i < n; i++, f3 = (f1%div + f2%div)%1234567) {
        f1 = f2;
        f2 = f3;
    }
    return f3;
}
int main() {
    cout << solution(100000000);
}