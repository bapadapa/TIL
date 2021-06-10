#include<iostream>
using namespace std;

class aPlusB5 {
private:
	int num1, num2;
public:
	void _setNum() {
		cin >> num1 >> num2;
	}
	void _answer() {
		while (!(num1==0 && num2==0 )) {
			cout << num1 + num2 << "\n";
			cin >> num1 >> num2;

			
		}
	}
};

int main(void) {
	ios_base::sync_with_stdio(false);

	aPlusB5 ap;
	ap._setNum();
	ap._answer();


}