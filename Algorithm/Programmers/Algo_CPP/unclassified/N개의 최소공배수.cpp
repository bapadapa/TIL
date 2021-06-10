//https://programmers.co.kr/learn/courses/30/lessons/12953
#include <iostream>

#include <string>
#include <vector>
using namespace std;

int LCM(int sNum, int bNum) {    
    if (bNum % sNum == 0)
        return bNum;
    int result = bNum;
    for (int i = 1; result % sNum != 0; i++) {
        result = bNum * i;
    }
    return result;
}

int solution(vector<int> arr) {    

    int answer = arr.front();
    for (auto elem : arr) { 
        if (answer <= elem) {
            answer = LCM(answer, elem);
        }
        else {
            answer = LCM(elem, answer);
        }
    }
    return answer;
}

int main() {
    cout << solution({ 2,6,8,14 });


}