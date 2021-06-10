#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	//	2차원 vector for문 사용법.
	/*for (vector<int> num : commands) {
		for (auto num2 : num)
			cout << num2 << endl;
	}*/

	vector<int> array = { 1, 5, 2, 6, 3, 7, 4 };
	vector<vector<int>> commands = { {2,5,3},{4,4,1},{1,7,3} };
	vector<int> answer;

	vector<int> tmp;


	for (vector<int> num : commands) {
		tmp.resize(num[1] - num[0] + 1);
		copy(array.begin() + num[0] - 1, array.begin() + num[1], tmp.begin());		sort(tmp.begin(), tmp.end());
		answer.push_back(tmp[num[2] - 1]);

	}

	for (auto elem : answer) {
		::cout << elem;
	}

}