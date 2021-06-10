//https://programmers.co.kr/learn/courses/30/lessons/12951

#include<iostream>

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
	string answer = "";
	bool isFirst = true;

	for (auto elem : s) {
		if (elem == ' ') {
			answer += ' ';
			isFirst = true;
		}
		else if (isFirst) {		
			answer += isdigit(elem) ? elem : toupper(elem);
			isFirst = false;				
		}
		else
			if (!isdigit(elem))
				answer  += tolower(elem);
	}

	cout << answer;

	return answer;
}
string solution1(string s) {
	string answer = "";

	if (!isdigit(s.front()))
		s.front() = toupper(s.front());

	for (int i = 1; i < s.length(); i++)
		s.at(i) = s.at(i - 1) == ' ' ? toupper(s.at(i)) : tolower(s.at(i));
	return s;
}

int main() {
	cout << solution1("aaaaa  aaa");

}

