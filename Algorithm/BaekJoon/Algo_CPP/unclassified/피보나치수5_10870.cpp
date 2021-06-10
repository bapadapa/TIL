//https://www.acmicpc.net/problem/10872

#include<iostream>

using namespace std;

class Answer {
private:
	int num;

public:
	int fibo(int N) {
		if (N == 0)
			return 0;
		else if (N == 1)
			return 1;
		return fibo(N-1) + fibo(N-2);
	}
	void solution() {
		cin >> num;
		cout << fibo(num);
	}

};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.solution();

}