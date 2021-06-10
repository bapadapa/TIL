//https://www.acmicpc.net/problem/1089
//다음 기회에...

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

class Answer {
private:
	int floors;
	double nums = 1;
	double sum = 0;
	vector<string> infoBoard;
	vector<vector<int>> possibleNum;
	vector<pair<int, bool>> plainBoard;
	vector<vector<int>> impossibleBoard = {
		{1},			{ 1,4 },   {},
		{ 1,2,3,7 },	{ -1 },	   { 5,6 },
		{ 1,7 },		{ 0,1,7 }, {},
		{ 1,3,4,5,7,9 },{ -1 },	   { 2 },
		{ 1,4 },		{ 4,7 },   {}
	};


public:

	void input() {
		cin >> floors;
		for (int i = 0; i < 5; i++) {
			string tmp;
			cin >> tmp;
			//4개로 묶음 만들기.
			infoBoard.push_back(tmp.append("."));
		}

		for (int i = 0; i < 10; i++)
			plainBoard.push_back(make_pair(i, true));
	}

	void checkPossibleNum() {
		vector<pair<int, bool>> checkNum;
		for (int k = 0; k < floors; k++) {
			checkNum = plainBoard;
			for (int num = 0; num < 10; num++) {
				for (int i = k * 4; i < k * 4 + 3; i++) {
					for (int j = 0; j < 5; j++) {
						if (infoBoard.at(j).at(i) == '#')
							for (auto elem : impossibleBoard.at(i % 4 + j * 3)) {
								if (elem == -1) {
									cout << -1;
									return;
								}
								if (elem == num) {
									checkNum.at(num).second = false;
									break;
								}
							}
						if (!checkNum.at(num).second)
							break;
					}
					if (!checkNum.at(num).second)
						break;
				}
			}
			vector<int> result;
			for (auto elem : checkNum) {
				if (elem.second) {
					result.push_back(elem.first);
				}
			}
			possibleNum.push_back(result);
		}
		for (int i = 0; i < possibleNum.size() -1;i++) {
			if (possibleNum.at(i).at(0) == possibleNum.at(i + 1).at(0) && possibleNum.at(i).at(0) == 0)
				possibleNum.at(i).erase(possibleNum.at(i).begin());
		}

		vector<int> numCnt;
		vector<int> numCombination;
		for (auto elem : possibleNum) {
			int cnt = 0;
			for (auto num : elem) {
				cnt++;
			}
			numCnt.push_back(cnt);
		}		
		for (int i = 0; i < numCnt.size(); i++) {
			int combi = 1;
			for (int j = 0; j < numCnt.size(); j++) {
				if (j == i)continue;
				combi *= numCnt.at(j);
			}
			numCombination.push_back(combi);
			nums *= combi;
		}
		if (floors == 1)
			nums = numCnt.at(0);
		for (int i = 0; i < possibleNum.size(); i++) {
			for (auto elem : possibleNum.at(i))
				sum += pow(10, possibleNum.size() - i - 1) * elem * numCombination.at(i);
		}

		for (int i = 0; i < possibleNum.size(); i++) {
			for (auto elem : possibleNum.at(i))
				sum += pow(10, possibleNum.size() - i - 1) * elem * numCombination.at(i);
		}
		cout << sum / nums;

	}

	void solution() {
		checkPossibleNum();
		
	}


};

int main() {
	Answer answer;
	answer.input();
	answer.checkPossibleNum();
}