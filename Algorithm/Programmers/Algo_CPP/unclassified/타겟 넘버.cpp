//https://programmers.co.kr/learn/courses/30/lessons/43165

#include<iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int target) {
	int answer = 0;
	vector<vector<int>> calcNum = { {0} };

	for (int i = 0; i < numbers.size(); i++) {
		vector<int> tmp;
		int num = numbers.at(i);
		for (int k = 0; k < calcNum.at(i).size(); k++) {
			int postNum = calcNum.at(i).at(k);
			tmp.push_back(postNum + num);
			tmp.push_back(postNum - num);
		}
		calcNum.push_back(tmp);
	}
	for(auto num : calcNum.at(calcNum.size()-1))
		if (num == target)
			answer++;

	return answer;
}

int main() {
	cout << solution({ 1,1,1,1,1 }, 3);
}