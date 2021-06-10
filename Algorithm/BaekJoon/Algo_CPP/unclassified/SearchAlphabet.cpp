/*
문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
*/
#include <iostream>
using namespace std;


class SearchAlphaber {
private:
	char alpha[101] = { ' ', };
	char alphabet = 'a';
	int cnt = 0;
	bool flag = false;

public:
	void answer() {
		cin >> alpha;
		//a~z를 tmp 에 삽입함.
		for (int i = 0; i < 26; i++) {
			flag = false;
			//tmp에 i씩 더한 alphabet값을 삽입함으로써 a~z로 만들어줌
			char tmp = alphabet + i;			
			//입력받은 값들의 갯수.
			for (int j = 0; j < sizeof(alpha); j++) {
				if (alpha[j] == tmp) {
					cout << j<< " ";
					flag = true;
					break;
				}
				else if (alpha[j] == NULL)
					break;
				else {					
					flag = false;					
				}
			}
			if (!flag)
				cout << -1<<" ";
		}
	}
};

int main(int argc, char* argv[]) {
	SearchAlphaber SA;
	SA.answer();

	return 0;

}
