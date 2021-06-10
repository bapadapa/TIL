/*
--출처--
프로그래머스

--문제 제목--
주식가격

--문제 설명--
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

--제한사항--
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

--입출력 예--
prices			return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
*/

#include<iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;   

    for (int i = 0; i < prices.size(); i++) {
        int cnt = 0;
        if (i + 1 == prices.size()) {
            answer.push_back(cnt);
            break;
        }            

        for (int j = i+1; j < prices.size(); j++) {
            if (prices[i] <= prices[j])
                cnt++;
            else {
                cnt++;
                break;
            }
                
        }        
        answer.push_back(cnt);
    }    
    return answer;
}

int main() {
    for (auto elem : solution({ 1, 2, 3, 2, 3 }))
        cout << elem << endl;


}