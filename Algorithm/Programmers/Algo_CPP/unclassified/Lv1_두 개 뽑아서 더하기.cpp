#include <string>
#include <vector>
#include<algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
	vector<int> answer;
	int cnt = 0;
	for (int i = 0; i < numbers.size() - 1; i++) {
		for (int j = i + 1; j < numbers.size(); j++) {
			answer.push_back(numbers[i] + numbers[j]);
		}
	}


	sort(answer.begin(), answer.end());

	for (int i = 0; i < answer.size() - 1; i++) {

		if (answer[i] == answer[i + 1])
			answer.erase(answer.begin() + i--);
	}
	return answer;

}