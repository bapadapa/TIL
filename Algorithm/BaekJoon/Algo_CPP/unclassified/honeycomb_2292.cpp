#include<iostream>

using namespace std;

class honeycomb {
private:
	int num;
	int cnt;
public:

	void answer() {
		cin >> num;
		if (num == 1) {		
			cout << 1;
			return;
		}
		num--;
		cnt = 0;
		while (num > 0) 
			num -= (6 * cnt++);
		
		cout << cnt;
				
		
	}
};

int main(int argc, char* argv[]) {
	honeycomb hc;
	hc.answer();
	return 0;

}