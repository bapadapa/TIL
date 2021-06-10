#include<iostream>

using namespace std;


class croatia {
private:
	char input[103];
	int cnt = 0;

public:

	void answer() {
		cin >> input;
		for (int i = 0; i < sizeof(input); i++) {
			if (input[i] == '\0')
				break;
			if (input[i] == 'd' && input[i + 1] == 'z' && input[i + 2] == '=')
				i += 2;
			else if (input[i + 1] == '-') {
				if (input[i] == 'c' || input[i] == 'd')
					i+=1;
			}
			else if (input[i + 1] == '=') {
				if (input[i] == 's' || input[i] == 'z' || input[i] == 'c')
					i +=1;
			}
			else if (input[i + 1] == 'j') {
				if (input[i] == 'l' || input[i] == 'n')
					i +=1;
			}
			cnt++;
		}
		cout << cnt;

	}
};

int main(int argc, char* argv[]) {
	croatia c;
	c.answer();
	return 0;

}