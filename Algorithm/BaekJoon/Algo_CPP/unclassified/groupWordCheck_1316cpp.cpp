#include<iostream>

using namespace std;


class groupWordCheck {
private:
	int n;
	char word[1001] = { 0, };
	bool flag = true;
	int cnt = 0;
public:
	void answer() {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> word;			
			bool checkApha[26] = { false };
			flag = true;
			
			for (int i = 0; i < sizeof(word); i++) {
				if (word[i] == '\0')
					break;

				if (checkApha[word[i] - 'a']) {
					flag = false;
					break;
				}					
				else
					checkApha[word[i] - 'a'] = true;

				while (word[i] == word[i + 1])
					++i;
			}
			if (flag)
				cnt++;

		}
		
		cout << cnt;
	}

};

int main(int argc, char* argv[]) {
	groupWordCheck gwc;
	gwc.answer();
	return 0;
}