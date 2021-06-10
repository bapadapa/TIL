#include<iostream>

using namespace std;


class breakeven_point {
private:
	int a, b, c;
	bool isOver = true;
public:
	void answer() {
		cin >> a, cin >> b, cin >> c;
		
		if (b >= c) {
			isOver = false;
			cout << -1;
			return;
		}

		
		cout << a/(c-b)+1;

	}
};

int main(int argc, char* argv[]) {

	breakeven_point bp;
	bp.answer();
	return 0;

}