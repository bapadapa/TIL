#include<iostream>
using namespace std;


class aPulseBMin8 {
private:
	int testCase;
	int num1, num2;
public:

	void _setNum() {
		cin >> testCase;

	}
	void _answer() {
		for (int i = 0; i < testCase; i++) {
			cin >> num1 >> num2;
			cout << "Case #" << i + 1 << ": "<<num1<<" + "<< num2 << " = " << num1 + num2 << "\n";
		}

	}
};

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	aPulseBMin8 apb;
	apb._setNum();
	apb._answer();
	return 0;

}
