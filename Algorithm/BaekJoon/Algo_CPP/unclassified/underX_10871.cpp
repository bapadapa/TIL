#include<iostream>
using namespace std;


class underX {
private:

	int testCase,underNum,tarfetNum;

public:

	void _setNum() {
		cin >> testCase >> underNum;

	}
	void _answer() {
		for (int i = 0; i < testCase; i++) {
			cin >> tarfetNum;
			if (tarfetNum < underNum)
				cout << tarfetNum << " ";

		}

	}
};

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	underX underX;
	underX._setNum();
	underX._answer();
	return 0;

}