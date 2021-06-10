#include<iostream>
using namespace std;

class average {
private:
	int score[1000] = { 0 , };
	int testCase;
	int max;
	double ave;
public:
	void _setNum() {
		cin >> testCase;

		cin >> score[0];
		max = score[0];
		ave = score[0];


	}

	void _answer() {

		for (int i = 1; i < testCase; i++) {
			cin >> score[i];
			ave += score[i];
			if (score[i] > max)
				max = score[i];
			
		}

		cout << (ave / max * 100) / testCase;;

	}
};

int main(void) {
	average a;
	a._setNum();
	a._answer();
	return 0;
}