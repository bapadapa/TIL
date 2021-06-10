//https://www.acmicpc.net/problem/10872

#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

class Answer {
private:
	int N, M;
	int ans = 0;
	pair<int, bool> card[100];

public:
	void blackJack(int cnt, int sum) {
		if (cnt == 3) {
			if (sum <= M)
				ans = abs(M - sum) < abs(M - ans) ? sum : ans;
			return;
		}
		for (int i = 0; i < N; i++) {
			if (!card[i].second) continue;
			card[i].second = false;
			blackJack(cnt + 1, sum + card[i].first);
			card[i].second = true;
		}
	}
	void solution() {
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			int num;
			cin >> num;
			card[i] = make_pair(num, true);
		}
		blackJack(0, 0);
		cout << ans;

	}

};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.solution();

}