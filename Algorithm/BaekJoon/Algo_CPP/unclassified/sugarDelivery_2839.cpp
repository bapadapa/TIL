#include<iostream>

using namespace std;

class sugarDelivery {
private:
	int sugar;
	int cnt3, cnt5;
	bool flag = true;

public:
	void answer() {
		cin >> sugar;

		cnt3 = 0;
		cnt5 = sugar / 5;
		
		while (cnt5 >= 0) {			
			if ((sugar - (cnt5 * 5)) % 3 == 0)
				cnt3 = (sugar - (cnt5 * 5)) / 3;			
			if (sugar == cnt3 * 3 + cnt5 * 5) {
				cout << cnt3 + cnt5;
				return;
			}
			cnt5--;
		}
		cout << -1;
	}
};

int main(int argc, char* argv) {
	sugarDelivery sd;
	sd.answer();
	return 0;
}