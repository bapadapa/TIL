//https://www.acmicpc.net/problem/1107


#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;


class Answer {
private:
	int curChannal = 100;
	int targetChannal;
	int brokenButtonCnt;
	int clickCnt = 0;

	bool brokenButton[10] = { false };

public:

	void input() {
		cin >> targetChannal >> brokenButtonCnt;
		for (int i = 0; i < brokenButtonCnt; i++) {
			int num;
			cin >> num;
			brokenButton[num] = true;
		}
		if (!brokenButton[0]) {
			clickCnt = abs(targetChannal - curChannal) < targetChannal + 1 ? abs(targetChannal - curChannal): targetChannal + 1;
		}
		else
			clickCnt = abs(targetChannal - curChannal);
	}

	void solution() {
		if (curChannal == targetChannal) {
			cout << clickCnt;
			return;
		}

		for (int i = 1; i < pow(10, to_string(targetChannal).length() + 1)-1; i++) {
			int press = 0;
			int num = i;
			while (num > 0) {
				if (brokenButton[num % 10]) {
					press = 0;
					break;
				}
				num /= 10;
				press++;
			}
			if (press != 0)
				clickCnt = clickCnt < press + abs(targetChannal - i) ? clickCnt : press + abs(targetChannal - i);
		}
		cout << clickCnt;

	}
};


int main() {
	Answer answer;
	answer.input();
	answer.solution();
}