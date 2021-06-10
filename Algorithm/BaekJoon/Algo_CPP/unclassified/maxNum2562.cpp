#include<iostream>
using namespace std;

class maxNum {
private:
	int max, rank;
	int tmp;
public:
	void _answer() {
		cin >> tmp;
		max = tmp;
		rank = 1;
		for (int i = 1; i < 9; i++) {
			cin >> tmp;
			if (tmp > max) {
				max = tmp;
				rank = i + 1;
			}
		}
		cout << max << "\n" << rank;
	}
};

int main(void) {
	maxNum mn;
	mn._answer();


	return 0;

}