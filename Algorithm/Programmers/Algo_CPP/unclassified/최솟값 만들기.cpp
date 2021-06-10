//https://programmers.co.kr/learn/courses/30/lessons/12941
//최솟값 만들기

#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<>());    
    while (!A.empty()) {
        answer+=A.back()* B.back();
        A.pop_back();
        B.pop_back();
    }   
    return answer;
}
