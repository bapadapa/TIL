#include <string>
#include <vector>
#include <math.h>

using namespace std;

int solution(int n) {
	int answer = 0;

	vector<int> ternary;
	int num = 1;

	while (true) {
		if (n == 0)
			break;
		ternary.push_back(n % 3);
		n /= 3;
	}
	while (true) {
		if (ternary.empty())
			break;
		answer += num * ternary.back();
		ternary.pop_back();
		num *= 3;
	}

	return answer;
}