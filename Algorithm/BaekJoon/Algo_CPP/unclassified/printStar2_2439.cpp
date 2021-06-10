#include<iostream>
using namespace std;


class printStar2 {
private:

	int num;
public:

	void _setNum() {
		cin >> num;

	}
	void _answer() {
		for (int i = 0; i < num; i++) {
			for (int k = num-i; k > 1; k--) {
				cout << " ";
			}
			for (int j = 0; j < i + 1; j++) {
				cout << "*";
			}

			cout << "\n";
		}

	}
};

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	printStar2 ps;
	ps._setNum();
	ps._answer();
	return 0;

}
