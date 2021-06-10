//https://www.acmicpc.net/problem/10872

#include<iostream>

using namespace std;

class Answer {
private:
	int num;

public:
	int factorial(int N) {
		if (N == 0) return 1;
		return factorial(N - 1)*N;
	}
	void solution() {
		cin >> num;
		cout << factorial(num);
	}

};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.solution();

}