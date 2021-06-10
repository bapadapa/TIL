#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;

	vector<int> a;
	a.assign(n + 2, 0);

	//잃어버린 친구들 고르기.
	for (auto elem : lost) {
		a[elem] --;
	}
	//여벌 있는 친구들 고르기
	for (auto elem : reserve) {
		a[elem] ++;
	}

	for (int i = 0; i <= n; i++) {
		if (a[i] == -1)
			if (a[i + 1] == 1) {
				a[i] = a[i + 1] = 0;
			}
			else if (a[i - 1] == 1) {
				a[i] = a[i - 1] = 0;
			}
	}
	for (auto elem : a) {
		if (elem >= 0)
			answer++;
	}
	return answer - 2;
}