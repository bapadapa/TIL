//https://www.acmicpc.net/problem/1456


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

const long long MAX = 10000001;
class Answer {
private:
	long long A, B;
	bool primeNum[MAX] = { false };
	vector <long long > prime;

public:
	void findPrime() {
		for (int i = 2; i < MAX; i++) {
			if (!primeNum[i])
				for (int j = 2 * i; j < MAX; j += i)
					primeNum[j] = true;
		}
		for (long long i = 2; i < MAX; i++) {
			if (!primeNum[i])
				prime.push_back(i);
		}
	}
	void check() {
		int cnt = 0;
		for (auto elem : prime) {
			long long exponentiation = elem;
			for (int i = 2; pow(elem, i) <= B; i++) {
				if (pow(elem, i) >= A)
					cnt++;
			}
		}
		cout << cnt;
	}

	void input() {
		cin >> A >> B;
		findPrime();
		check();
	}
};

int main() {
	Answer answer;
	answer.input();
}