#include<iostream>
using namespace std;

class plusCycle {
private:
	int num,cnt,nextNum;

public:
	void _setNum() {
		cin >> num;
		cnt = 0;
	}
	void _answer() {
		nextNum = (num % 10 + num / 10)%10 + (num%10*10);
		cnt++;
		while (true) {
			
			if (nextNum == num)
				break;
			nextNum = (nextNum % 10 + nextNum / 10)%10 + (nextNum % 10 * 10);
		
			cnt++;
			
		}
		cout << cnt;
	}
};

int main(void) {
	ios_base::sync_with_stdio(false);

	plusCycle pc;
	pc._setNum();
	pc._answer();


}