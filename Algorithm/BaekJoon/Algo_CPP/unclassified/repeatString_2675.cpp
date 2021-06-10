#include<iostream>

using namespace std;

class repeatString {
private:
	int testcase;

public:
	void answer() {
		cin >> testcase;
		for (int i = 0; i < testcase; i++) {
			char alpha[21] = { ' ', };
			int cnt;
			cin >> cnt;
			cin >> alpha;
			if (cnt > 0 && cnt <= 8)
				for (int j = 0; j < sizeof(alpha); j++)
					for (int k = 0; k < cnt; k++)
						if (alpha[j] == NULL)
							break;
						else
							cout << alpha[j];
			cout << endl;
		}

	}


};

int main(int argc, char** argv) {
	repeatString rs;
	rs.answer();
	return 0;

}