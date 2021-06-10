//https://programmers.co.kr/learn/courses/30/lessons/42747
#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
	//최대 점수
	int answer = citations.size(),cnt;
	
	sort(citations.begin(), citations.end() , greater<>());
	while (answer) {
		cnt = 0;
		for (int i = 0; i < citations.size(); i++) {
			if (answer <= citations[i]) {
				cnt++;
			}
		}
		if (cnt >= answer) {
			break;
		}
		answer--;
	}
	return answer;
}

int main() {
	cout << endl << solution({ 4,4,4 });
}