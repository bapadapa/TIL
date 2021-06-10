
/*
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

출력값
1. Mississipi  --> ?
2. zZa -->Z
3. z -->Z
4. baaa -->A
*/
#include<iostream>
#include<stdlib.h>
using namespace std;

class studyString {
private:
	char str[1000001];
	int  strCheck[26] = { 0, };
	int max = 0;
	bool flag = true;
public:

	void answer() {
		cin >> str;

		for (int i = 0; i < sizeof(str); i++) {
			//입력 받은 값이 더 이상 없다면 종료.
			if (!str[i])
				break;

			//대문자면
			if ((str[i] - 'a') < 0) {
				if (str[i] - 'A' >= 0) {
					strCheck[str[i] - 'A'] += 1;
					continue;
				}
			}
			//소문자면
			else {
				strCheck[str[i] - 'a'] += 1;
			}
		}
		for (int i = 0; i < 26; i++) {
			if (strCheck[max] < strCheck[i])
				max = i;
		}
		for (int i = 0; i < 26; i++) {
			if (i == max)
				continue;
			if (strCheck[max] == strCheck[i]) {
				cout << '?';
				flag = false;
				break;
			}
		}

		if (flag)
			cout << char(max + 'A');
	}

};

int main(int argc, char* argv[]) {
	studyString ss;
	ss.answer();
	return 0;
}