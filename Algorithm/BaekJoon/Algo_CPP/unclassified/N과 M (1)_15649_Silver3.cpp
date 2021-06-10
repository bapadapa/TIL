//https://www.acmicpc.net/problem/15649

#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Answer {
private:
	int printCnt, N;
	pair<int, bool> nums[9];

public:
	void input() {
		cin >> N >> printCnt;
		for (int i = 0; i < N; i++) {
			nums[i] = make_pair(i + 1, false);
		}
		solution(0, "");
	}
	void solution(int cnt, string answer) {
		if (cnt == printCnt)
			cout << answer << "\n";
		for (int i = 0; i < N; i++) {
			if (nums[i].second == true) continue;
			nums[i].second = true;
			solution(cnt + 1, answer + (char)(nums[i].first + '0') + " ");
			nums[i].second = false;
		}
	}

};
int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	Answer answer;
	answer.input();
}