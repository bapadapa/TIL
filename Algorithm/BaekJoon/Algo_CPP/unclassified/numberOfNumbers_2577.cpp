#include<iostream>
using namespace std;

class numberOfNumbers {
private:
	int numA, numB, numC;
	int mul;
	int cnt[10] = { 0, };
public:
	void _answer() {
		cin >> numA >> numB >> numC;
		mul = numA * numB*numC;
		
		while (mul>0) {
			int tmp = mul % 10;
			
			cnt[tmp] += 1;
			mul /= 10;
		}
		for (int i = 0; i < 10; i++) {
			cout << cnt[i] << endl;
		}
	}
	
};


int main(void) {
	numberOfNumbers non;
	non._answer();
}