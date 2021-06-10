#include<iostream>

#include <string>
#include <vector>
#include<stdlib.h>
using namespace std;

int compress(string s, int unit) {
	string answer = "";
	string preStr = s.substr(0, unit);
	string curStr;
	int length = s.length();
	int cnt = 1;
	for (int i = unit; i <= length; i += unit) {
		if (i + unit <= length) {
			curStr = s.substr(i, unit);
			if (curStr.compare(preStr) == 0) 
				cnt++;			
			else {
				if (cnt == 1) 
					answer.append(preStr);				
				else 
					answer.append(to_string(cnt) + preStr);
				cnt = 1;
			}
		}
		else {
			if (cnt == 1) 
				answer.append(preStr+s.substr(i, length - i));			
			else {
				if (i != length) 
					answer.append(to_string(cnt) + preStr + s.substr(i, length - i));
				
				else				
					answer.append(to_string(cnt) + preStr);				
			}
			break;
		}
		preStr = curStr;
	}
	return answer.length();
}

int solution(string s) {
	int answer = s.length();
	for (int i = 1; i < s.length() / 2+1; i++) {
		int length = compress(s, i);		
		answer = answer < length ? answer : length;
	}
	return answer;
}

int main() {
	cout << "answer = " << solution("aabbaccc");
}