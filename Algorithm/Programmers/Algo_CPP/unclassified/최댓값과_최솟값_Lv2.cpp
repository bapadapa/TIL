//https://programmers.co.kr/learn/courses/30/lessons/12939
#include<iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    s.push_back(' ');
    vector<int> answer;
    string token;
    int pos = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            answer.push_back(stoi(s.substr(pos, i-pos).c_str()));
            pos = i + 1;
        }
    }
    sort(answer.begin(), answer.end());
    return to_string(answer.front()) + " " + to_string(answer.back());
}
int main() {
    
    cout << solution("1 2 3 4");
}