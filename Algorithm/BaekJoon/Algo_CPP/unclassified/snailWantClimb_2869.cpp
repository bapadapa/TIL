#include<iostream>
#include<cmath>
using namespace std;

class snailWantClimb {
private:
	int a, b, v;

public:
	void answer() {
		cin >> a, cin >> b, cin >> v;
		
		int tmp = 0;
		if(((v - b) % (a - b)) == 0 )
			tmp = ((v - b) / (a - b));
		else 
			tmp = ((v - b) / (a - b))+1;
		
		cout << tmp;
			

	}
};

int main(int argc, char* argv[]) {
	snailWantClimb swc;
	swc.answer();
	return 0;
}
