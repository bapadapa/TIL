//https://www.acmicpc.net/problem/1018


#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
#define min(A,B){A<B?A:B}
class Answer {
private:
	int R, C;
	int ans = 64;
	string board[50];
	string startW = "WBWBWBWB";
	string startB = "BWBWBWBW";

public:
	void checkW(int xPos, int yPos) {
		int cnt = 0;
		for (int i = xPos; i < xPos + 8; i++) {
			for (int j = yPos; j < yPos + 8; j++) {
				if (i % 2 == 0) {
					if (board[i][j] != startW[j-yPos])
						cnt++;
				}
				else
					if (board[i][j] != startB[j-yPos])
						cnt++;
			}
		}
		ans = min(ans, cnt);
	}
	void checkB(int xPos, int yPos) {
		int cnt = 0;
		for (int i = xPos; i < xPos + 8; i++) {
			for (int j = yPos; j < yPos + 8; j++) {
				if (i % 2 == 0) {
					if (board[i][j] != startB[j-yPos])
						cnt++;
				}
				else
					if (board[i][j] != startW[j-yPos])
						cnt++;
			}
		}
		ans = min(ans, cnt);
	}

	void solution() {
		for (int i = 0; i < R - 7; i++) {
			for (int j = 0; j < C - 7; j++) {
				checkB(i, j);
				checkW(i, j);
			}
		}
		cout << ans;
	}

	void input() {
		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			cin >> board[i];
		}
		solution();
	}
};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.input();

}