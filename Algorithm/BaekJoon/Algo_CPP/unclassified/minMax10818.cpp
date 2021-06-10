#include<iostream>
using namespace std;

class minMax {
private:
	int testCase;

public:

	void _answer() {
		cin >> testCase;
		int max, min,tmp;

		cin >> max;
		min = max;

		for (int i = 1; i < testCase; i++) {
			cin >> tmp;
			if (tmp > max)
				max = tmp;
			else if (tmp < min)
				min = tmp;

		}
		cout << min << " " << max;
	}


};

int main(void) {
	minMax mm;
	mm._answer();
	return 0;
}



