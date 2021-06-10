#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
	vector<int> answer;
	vector<int> stu1 = { 1,2,3,4,5 };
	vector<int> stu2 = { 2,1,2,3,2,4,2,5 };
	vector<int> stu3 = { 3,3,1,1,2,2,4,4,5,5 };
	int score[3] = { 0, };

	for (auto i = 0; i < answers.size(); i++) {
		if (answers[i] == stu1[i % 5]) {
			score[0] ++;
		}
		if (answers[i] == stu2[i % 8]) {
			score[1] ++;
		}
		if (answers[i] == stu3[i % 10]) {
			score[2] ++;
		}
	}
	int maxscore = max(max(score[0], score[1]), score[2]);

	for (int i = 0; i < 3; i++) {
		if (score[i] == maxscore)
			answer.push_back(i + 1);
	}

	return answer;
}