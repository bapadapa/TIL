//https://www.acmicpc.net/problem/2231

#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

#define min(A,B){A<B?A:B}
class Answer {
private:
	int N;
	int ans = -1;

public:
	int sumDigit(int num) {
		int sum = 0;
		while (num != 0) {
			sum += num % 10;
			num /= 10;
		}
		return sum;
	}
	void solution() {
		cin >> N;
		int tmp = N;
		do {
			if (tmp + sumDigit(tmp) == N)
				if (ans == -1) ans = tmp;
				else ans = min(ans, tmp);
		} while (tmp--);
		if (ans == -1)
			cout << 0;
		else
			cout << ans;
	}
};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.solution();

}