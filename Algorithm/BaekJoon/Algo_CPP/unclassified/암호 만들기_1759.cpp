//https://www.acmicpc.net/problem/1759

#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool compair(pair<char, bool> X, pair<char, bool> Y) { return X.first < Y.first; }

class Answer {
private:
	int L,C;	
	vector<pair<char, bool>> charVec;


public:
	bool check(char word) {
		char tmp[] = { 'a', 'e', 'i', 'o', 'u' };
		for (auto vowel : tmp)
			if (word == vowel) return true;
		return false;
	}

	string makePassword() {
		string password = "";
		for (int i = 0; i < C; i++) {
			if (charVec[i].second == true) {
				password += charVec[i].first;
			}
		}
		return password;
	}
	void DFS(int idx, int cnt, int mo, int ja) {

		if (cnt == L) {
			if (mo > 0 && ja > 1)
				cout << makePassword() << endl;

			return;
		}
		for (int i = idx; i < C; i++) {
			if (charVec[i].second == true)continue;
			charVec[i].second = true;
			if (check(charVec[i].first))
				DFS(i, cnt + 1, mo + 1, ja);
			else
				DFS(i, cnt + 1, mo, ja + 1);
			charVec[i].second = false;
		}
	}

	void input() {
		cin >> L >> C;
		for (int i = 0; i < C; i++) {
			char tmp;
			cin >> tmp;
			charVec.push_back(make_pair(tmp, false));
		}
		sort(charVec.begin(), charVec.end(), compair);
		for (int i = 0; i < charVec.size() - 1; i++)
			if (charVec.at(i).first == charVec.at(i + 1).first)
				charVec.erase(charVec.begin() + i);
		C = charVec.size();
	}
	void solution() {
		DFS(0, 0, 0, 0);
	}
};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.input();
	answer.solution();

}