//https://www.acmicpc.net/problem/2609

#include<iostream>

using namespace std;


class Answer {
private:
	int A, B;

public:
	//최대 공약수
	void gcd(int num1, int num2) {
		int gcdNum = num1 < num2 ? num1 : num2;
		while (gcdNum) {
			if (num1 % gcdNum == 0 && num2 % gcdNum == 0)
				break;
			gcdNum--;
		}
		cout << gcdNum << endl;

	}
	//최소 공배수
	void lcm(int num1, int num2) {
		int i = 1;
		int j = 1;
		while (num1 * i != num2 * j) {
			if (num1 * i < num2 * j) {
				i++;
			}
			else {
				j++;
			}
		}
		cout << num1 * i;
	}
	//최대 공약수
	int gcd2(int num1, int num2) {
		while(num2 != 0){
			int tmp = num2;
			num2 = num1% num2;
			num1 = tmp;
		}
		return num1;
	}
	//최소 공배수
	int lcm2(int num1, int num2) {
		return num1 * num2 / gcd2(num1, num2);
	}

	//최대 공약수
	int gcdR(int num1, int num2) {
		if (num2 == 0)return num1;
		return gcdR(num2, num1 % num2);
	}
	//최소 공배수
	int lcmR(int num1, int num2) {
		return num1 * num2 / gcdR(num1, num2);
	}


	void input() {
		cin >> A >> B;
		cout << gcd2(A, B) << endl << lcm2(A, B);

	}


};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	Answer answer;
	answer.input();


}