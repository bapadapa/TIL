//https://programmers.co.kr/learn/courses/30/lessons/42626
//´õ ¸Ê°Ô

#include <iostream>

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
	int answer = 0;
	int tmp;
	bool isPerfect = false;
	priority_queue<int, vector<int>, greater<int> > q;
	for (auto elem : scoville) {
		q.push(elem);
	}
	while (q.top() < K) {
		tmp = q.top();
		q.pop();
		tmp += q.top() * 2;
		q.pop();
		if (q.size() == 1 && q.top() < K)
			return -1;
		q.push(tmp);
		answer++;
	}
	return answer;
}
