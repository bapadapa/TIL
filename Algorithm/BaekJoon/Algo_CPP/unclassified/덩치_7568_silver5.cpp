//https://www.acmicpc.net/problem/7568


#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Answer {
private:
	int n;
	int weight[50];
	int hight[50];
	
public:
	void solution() {		
		for (int i = 0; i < n; i++) {
			int num = 1;
			for (int j = 0; j < n; j++) {
				if (i == j) continue;
				if (weight[i] < weight[j] && hight[i] < hight[j])
					num++;
			}
			cout << num << " " ;
		}		
	}

	void input() {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> weight[i] >> hight[i];
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