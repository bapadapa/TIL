#include<iostream>
using namespace std;


class fibonacci {
private:
	int zeroCnt[41] = { 0, };
	int oneCnt[41] = { 0, };
	int num;

public:

	void _setNum() {
		cin >> num;
		zeroCnt[0] = 1;
		oneCnt[0] = 0;
	}

	void _answer() {
		//±ÔÄ¢ 
		for (int j = 1; j <= num; j++) {
			zeroCnt[j] = oneCnt[j - 1];
			oneCnt[j] = zeroCnt[j - 1] + oneCnt[j - 1];
		}
	}

	void _print() {
			cout << zeroCnt[num] << " " << oneCnt[num] << endl;
	}
};
int main(void) {
	int caseCnt;
	fibonacci fibo;
	cin >> caseCnt;
	for (int i = 0; i < caseCnt; i++) {
		fibo._setNum();
		fibo._answer();
		fibo._print();
	}

}
