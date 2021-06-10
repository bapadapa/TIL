#include<iostream>
using namespace std;

class scale {
private:
	int cntA, cntD;

	int enterScale[8] = { 0, };
public:
	void _answer() {
		cntA = cntD = 0;
		for (int i = 0; i < 8; i++) {
			cin >> enterScale[i];
		}
		for (int i = 0; i < 8; i++) {
			if (enterScale[i] == i + 1) {
				cntA++;
			}
			else if (enterScale[i] ==( 8 - i ))
				cntD++;
		}

		if (cntA == 8) {

			cout << "ascending";
		}
		else if (cntD == 8) {
			cout << "descending";
		}
		else
			cout << "mixed";

	}
};

int main(void) {
	scale c;
	c._answer();
	return 0;
}

