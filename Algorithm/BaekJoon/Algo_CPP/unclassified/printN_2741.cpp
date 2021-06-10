#include<iostream>

using namespace std;

class printN {
private:
	int n;

public:
	void _setNum() {
		cin >> n;

	}
	void _answer() {
		for (int i = 0; i < n; i++)
			_print(i + 1);
	}
	void _print(int n) {
		cout << n << "\n";

	}

};

int main(void) {
	printN pn;
	pn._setNum();
	pn._answer();
	
}