//https://www.acmicpc.net/problem/20302

#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

class Answer {
private:
	int cnt;
	double result;
	int Nums[100001] = { 0 };

public:
	void mul(int n) {
		for (int i = 2; i < (int)sqrt(n) + 1; i++) {
			while (!(n % i)) Nums[i]++, n /= i;
			if (n == 1)break;
		}
		if (n > 1)
			Nums[n]++;
	}
	void div(int n) {
		for (int i = 2; i < (int)sqrt(n) + 1; i++) {
			while (!(n % i)) Nums[i]--, n /= i;
			if (n == 1)break;
		}
		if (n > 1)
			Nums[n]--;
	}

	string solution() {
		cin >> cnt;
		int num;
		char _oper;
		cin >> num;
		if (num == 0) return "mint chocolate";
		mul(abs(num));
		for (int i = 0; i < cnt - 1; i++) {
			cin >> _oper >> num;
			if (num == 0) return "mint chocolate";
			num = abs(num);
			if (_oper == '*')
				mul(num);
			else
				div(num);
		}
		for (int i = 2; i < 100001; i++) {
			if (Nums[i] < 0)
				return "toothpaste";
		}
		return "mint chocolate";
	}
};
int main() {
	cin.tie(NULL); cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	cout << answer.solution();
}