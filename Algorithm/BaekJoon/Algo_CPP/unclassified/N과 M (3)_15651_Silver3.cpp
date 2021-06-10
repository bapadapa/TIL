//https://www.acmicpc.net/problem/15651

#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Answer {
private:
	int printCnt, N;
	int nums[9];
	int *combi;

public:
	void input() {
		cin >> N >> printCnt;
		for (int i = 0; i < N; i++) {
			nums[i] = i + 1;
		}
		combi = new int[N];
		solution(0);
		
	}
	void solution(int depth) {
		if (depth == printCnt) {
			for (int i = 0; i < printCnt; i++) {
				cout << combi[i] << " ";
			}
			cout << "\n";
			return;
		}
		for (int i = 0; i < N; i++) {
			combi[depth] = nums[i];
			solution(depth + 1);
		}	
	}

};
int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	Answer answer;
	answer.input();
}