#include<iostream>
using namespace std;


class dial {
private:
	char number[16];
	int time = 0;
public:
	void answer() {
		cin >> number;
		for (int i = 0; i < sizeof(number); i++) {
			if (number[i] == '\0')
				break;
			char tmp = number[i];			
			time += search(tmp - 'A');			
		}
		cout << time;
	}

	int search(char n) {
		if (n == 18) {
			return n / 3 + 2;
		}
		else if (n > 20 && n < 22) {
			return n / 3 + 2;
		}
		else if( n > 23)	
			return n / 3 + 2;
		else
			return n / 3 + 3;
		

	}
};

int main(int argc, char* argv) {
	dial D;
	D.answer();
	return 0;

}