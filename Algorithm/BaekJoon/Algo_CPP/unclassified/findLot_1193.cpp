#include<iostream>

using namespace std;

class findLot {
private:
	int num;
	int cnt;
	int a, b;
	bool flag = true;
public:
	void answer() {
		cin >> num;
		a = b = 1;

		if (num == 1) {
			cout << a << "/" << b;
			return;
		}			
		
		for (int i = 1; i < num; i++) {
			
			if (a == 1 && flag) {
				b++;
				flag = false;
				continue;
			}
			else if (b == 1 && !flag) {
				a++;
				flag = true;				
				continue;
			}

			if (!flag) {
				a++;
				b--;
			}
			else{
				b++;
				a--;
			}

			
			
		}
		cout << a << "/" << b;
	}
};

int main(int argc, char* argv[]) {
	findLot fl;
	fl.answer();
	return 0;
}