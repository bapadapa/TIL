#include<iostream>
using namespace std;

class aPlusB4{
private:
	int num1, num2;
	
public:
	void _setNum() {
		cin >> num1 >> num2;
	}
	void _answer() {
		while (true) {
			cout << num1 + num2 << "\n";
			cin >> num1 >> num2;
			//EOF받아오기.
			if (cin.eof()) {
				break;
			}
		}
	}
};

int main(void) {
	ios_base::sync_with_stdio(false);

	aPlusB4 ap;
	ap._setNum();
	ap._answer();


}