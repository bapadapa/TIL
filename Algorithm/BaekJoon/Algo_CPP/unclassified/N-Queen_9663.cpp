//https://www.acmicpc.net/problem/9663
#include<iostream>
#include<vector>
#include<time.h>
#include<algorithm>

#include<stdio.h>

using namespace std;


class answer1 {
private:
	int count = 0;
	int n = 0;
	bool check = false;
	int x, y;

public:
	void test() {
		clock_t startTime, endTime;
		//	cin >> n;
		bool a[14][14];
		fill(a[0], a[0] + 14 * 14, true);
		for (n = 1; n < 12; n++) {
			count = 0;
			startTime = clock();
			vector<vector<bool>> board;
			board.resize(n, vector<bool>(n, true));
			makeBoard(board, 0, 0);
			endTime = clock();
			cout << "size = " << n << " total = " << count << " Time = " << (double)(endTime - startTime) << endl;

		}
		//cout << count << endl;
	}

	void checkPos(vector<vector<bool>> board, int row, int col) {
		if (row == n - 1) {
			count++;
			return;
		}
		if (find(board.at(row + 1).begin(), board.at(row + 1).end(), true) == board.at(row + 1).end())
			return;

		for (int i = row; i < n; i++) {
			board.at(i).at(col) = false;
		}
		x = row; y = col;
		while (++x < n && --y >= 0) {
			board.at(x).at(y) = false;
		}
		x = row; y = col;
		while (++x < n && ++y < n) {
			board.at(x).at(y) = false;
		}
		for (int i = 0; i < n; i++)
			if (board.at(row + 1).at(i)) {
				makeBoard(board, ++row, i);
				break;
			}
	}
	void makeBoard(vector<vector<bool>> board, int row, int col) {
		for (int i = 0; i < n; i++)
			if (board.at(row).at(i))
				checkPos(board, row, i);
	}
};


class answer2 {
private:
	int n;
	int cnt = 0;
	vector<bool> lDiagonal, rDiagonal, vertical;
public:

	void test() {

		clock_t startTime, endTime;
		for (n = 1; n < 12; n++) {
			cnt = 0;
			startTime = clock();
			vertical.resize(n, false);
			lDiagonal.resize(n * 2 - 1, false);
			rDiagonal.resize(n * 2 - 1, false);
			this->solution(0);
			endTime = clock();
			cout << "size = " << n << " total = " << cnt << " Time = " << (double)(endTime - startTime) << endl;

		}
	}

	void answer() {
		cin >> n;
		vertical.resize(n, false);
		lDiagonal.resize(n * 2 - 1, false);
		rDiagonal.resize(n * 2 - 1, false);
		solution(0);
		cout << cnt;
	}
	void solution(int col) {
		if (col == n) {
			cnt++;
			return;
		}
		for (int row = 0; row < n; row++) {
			if (!(vertical.at(row) || lDiagonal.at(col + row) || rDiagonal.at(col - row + n - 1))) {
				vertical.at(row) = lDiagonal.at(col + row) = rDiagonal.at(col - row + n - 1) = true;
				solution(col + 1);
				vertical.at(row) = lDiagonal.at(col + row) = rDiagonal.at(col - row + n - 1) = false;

			}

		}



	}

};



class answer3 {
private:
	bool vertical[14], rDiagonal[27], lDiagonal[27];
	int n;
	int cnt = 0;
	
public:

	void test() {

		clock_t startTime, endTime;
		for (n = 1; n < 15; n++) {
			cnt = 0;
			startTime = clock();
			fill_n(vertical, size(vertical), false);
			fill_n(lDiagonal, size(lDiagonal), false);
			fill_n(rDiagonal, size(rDiagonal), false);
			solution(0);
			endTime = clock();
			cout << "size = " << n << " total = " << cnt << " Time = " << (double)(endTime - startTime) << endl;

		}
	}

	void ans() {
		cin >> n;
		fill_n(vertical, size(vertical), false);
		fill_n(lDiagonal, size(lDiagonal), false);
		fill_n(rDiagonal, size(rDiagonal), false);
		solution(0);
		cout << cnt;
	}
	void solution(int row) {
		if (row == n) {
			cnt++;
			return;
		}
		for (int col = 0; col < n; col++)
			if (!(vertical[col] || lDiagonal[row + col] || rDiagonal[row - col + n - 1])) {
				vertical[col] = lDiagonal[row + col] = rDiagonal[row - col + n - 1] = true;
				solution(row + 1);
				vertical[col] = lDiagonal[row+ col] = rDiagonal[row - col + n - 1] = false;
			}
	}

};

int main() {
	answer1 answer1;
	cout << "대각선, 세로 변경하며 찾기" <<endl;
	answer1.test();
	answer2 answer2;
	cout << "\n벡터로 검색" << endl;
	answer2.test();

	answer3 answer3;
	cout << "\n배열로 검색" << endl;
	answer3.test();
	
}