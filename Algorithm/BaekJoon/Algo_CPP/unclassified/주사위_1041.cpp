
//https://www.acmicpc.net/problem/1041


#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
#define MIN(X,Y) (X<Y ? X:Y)
class Answer {
private:
	int min = 0;
	long long minCase[3];
	long long dice[6];
	long long N = 0;
public:
	void input() {
		cin >> N;
		for (int i = 0; i < 6; i++)
			cin >> dice[i];
	}
	void checkMin() {
		minCase[0] = MIN(dice[0], dice[5]);
		minCase[1] = MIN(dice[1], dice[4]);
		minCase[2] = MIN(dice[2], dice[3]);
		sort(minCase, minCase + 3);
		minCase[2] += minCase[0] + minCase[1];
		minCase[1] += minCase[0];
	}
	void solution() {
		long long answer = 0;
		if (N == 1) {
			sort(dice, dice + 6);
			for (int i = 0; i < 5; i++) {
				answer += dice[i];
			}
			cout << answer;
		}
		else {
			checkMin();
			answer += minCase[0] * ((N - 1) * (N - 2) * 4 + (N - 2) * (N - 2));
			answer += minCase[1] * (8 * N - 12);
			answer += minCase[2] * 4;
			cout << answer;
		}
	}
};

int main() {
	//입출력 속도.
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.input();
	answer.solution();
}