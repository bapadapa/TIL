#include<iostream>
using namespace std;

class printNDescending {
private:
	int n;
public:
	void _setNum() {
		cin >> n;
	}
	void _answer() {
		for (int i = n; i > 0; i--) {
			cout << i << "\n";
		}
	}
};

int main(void) {
	printNDescending pnd;
	ios_base::sync_with_stdio(false);
	pnd._setNum();
	pnd._answer();

	return 0;

}