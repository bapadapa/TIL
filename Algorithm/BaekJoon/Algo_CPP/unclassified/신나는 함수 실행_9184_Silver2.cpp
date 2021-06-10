//https://www.acmicpc.net/problem/9184

#include<iostream>
#include<vector>
using namespace std;

class Answer {
private:
	vector<vector<int>> Nums;
	int dpNum[101][101][101] = { 0 };
public:
	void input() {
		while (true) {
			int n1, n2, n3;
			cin >> n1 >> n2 >> n3;
			if (n1 == -1 && n2==-1 && n3 == -1)
				break;
			vector<int> tmp{ n1,n2,n3 };
			Nums.push_back(tmp);
		}
		solution();
	}
	void solution() {
		for (auto elem : Nums) {
			cout << "w(" << elem.at(0) << ", " << elem.at(1) << ", " << elem.at(2) << ") = " << w(elem.at(0), elem.at(1), elem.at(2))<<endl;
		}

	}
	int w(int a, int b, int c) {
		if (dpNum[a + 50][b + 50][c + 50] == 0) {
			if (a <= 0 || b <= 0 || c <= 0)
				return 1;

			if (a > 20 || b > 20 || c > 20)
				return w(20, 20, 20);
		
			if (a < b && b < c)
				dpNum[a + 50][b + 50][c + 50]=  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
		
			dpNum[a + 50][b + 50][c + 50]= w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
		}
		return dpNum[a + 50][b + 50][c + 50];		
	}

};

int main() {
	cin.tie(NULL), cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	Answer answer;
	answer.input();


}