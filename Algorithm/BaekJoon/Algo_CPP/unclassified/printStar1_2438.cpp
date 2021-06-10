#include<iostream>
using namespace std;


class printStar1 {
private:

	int num;
public:

	void _setNum() {
		cin >> num;

	}
	void _answer() {
		for (int i = 0; i < num; i++) {
			for (int j = 0; j < i+1; j++)
				cout << "*";
			cout << "\n";
		}

	}
};

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	printStar1 ps;
	ps._setNum();
	ps._answer();
	return 0;

}
