#include<iostream>
using namespace std;


class selfNumber {

private:
	bool selfNum[10001];
	int cnt = 1;
public:
	void _answer() {

		//ÃÊ±âÈ­.
		for (int i = 0; i < 10001; i++) {
			selfNum[i] = true;
		}

		for (int i = 1; i < 10001; i++) {
			if (_selfSum(i) < 10001)
				selfNum[_selfSum(i)] = false;
		}

		for (int i = 1; i < 10001; i++) {
			if (selfNum[i])
				cout << i << endl;
		}


	}


	int _selfSum(int num) {
		int sum = num;
		while (num > 0) {
			sum += num % 10;
			num = num / 10;
		}

		return sum;
	}
};
int main(void) {
	selfNumber sn;
	sn._answer();

	return 0;


}