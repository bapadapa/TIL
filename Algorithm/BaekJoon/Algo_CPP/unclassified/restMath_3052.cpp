#include<iostream>
using namespace std;

class restMath {
private:
	bool rest[42];
	int tmp;
	int restCnt = 0;
public:
	void _answer() {
		for (int i = 0; i < 42; i++) {
			rest[i] = false;
		}
		for (int i = 0; i < 10; i++) {
			cin >> tmp;
			rest[tmp % 42] = true;
		}
		for (int i = 0; i < 42; i++) {
			if (rest[i])
				restCnt++;
		}
		cout << restCnt;
	}
};

int main(void) {
	restMath rm;
	rm._answer();
	return 0;
}

