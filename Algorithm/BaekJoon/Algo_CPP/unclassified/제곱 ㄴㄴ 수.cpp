//https://www.acmicpc.net/problem/1016

#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;
const long long MAX = 1000001;
class Answer {
private:
	long long A, B;
	bool _isExponentiationNum[MAX] = { false };

public:
	void input() {
		cin >> A >> B;
		check();
	}
	void check() {
		for (long long i = 2; i * i <= B; i++) {
			long long curExponent = i * i;
			long long _time =
				(A / curExponent) * curExponent >= A ?
				A / curExponent : (A / curExponent) + 1;
			long long num = curExponent * _time;
			while (num <= B) {
				_isExponentiationNum[num - A] = true;
				num += curExponent;
			}
		}
		cout << count(_isExponentiationNum, _isExponentiationNum + B - A + 1, false);
	}

};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	Answer answer;
	answer.input();

}