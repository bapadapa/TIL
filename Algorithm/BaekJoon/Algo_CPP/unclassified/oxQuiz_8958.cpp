#include<iostream>
#include<string>
using namespace std;

class oxQuiz {
private:
	char oxArr[81];
	int testCase;
	int length;
	int score;
	int score_sum;
	bool flag = true;
public:
	void _answer() {
		cin >> testCase;


		//테스트 케이스만큼 반복.


		for (int i = 0; i < testCase; i++) {

			int cnt = 0;
			score_sum = score = 0;
			while (true) {
				char ch;

				//cini.get()으로 받아야 \n을 읽어드림.
				cin.get(ch);

				//최초 1회 \n값 안 받기.
				if (flag) {
					flag = false;
					continue;
				}

				if (ch == '\n')
					break;

				oxArr[cnt] = toupper(ch);

				for (int j = 0; j <= cnt; j++) {
					if (oxArr[j] == 'O')
						score += 1;
					else
						score = 0;
					score_sum += score;

				}

			}
			cout << score_sum << endl;


		}

	}

};

int main(void) {
	oxQuiz oxq;
	oxq._answer();

	return 0;

}
