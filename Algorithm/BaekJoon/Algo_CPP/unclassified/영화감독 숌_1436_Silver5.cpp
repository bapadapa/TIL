//https://www.acmicpc.net/problem/1436

#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

class Answer {
private:
	int N;

public:
	void input() {
		cin >> N;
		solution();
	}
	void solution() {
		int Num = 666;
		int cnt = 0;
		while (cnt < N) {
			string tmp = to_string(Num++);
			for (int i = 0; i < size(tmp)-2; i++) {
				if (tmp[i] == '6' && tmp[i + 1] == '6' && tmp[i + 2] == '6') {
					cnt++;
					break;
				}
			}
		}
		cout << Num-1;
	}

};
int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.input();
}