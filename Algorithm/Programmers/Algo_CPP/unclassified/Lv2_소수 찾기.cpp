/*
--출처--
프로그래머스

소수 찾기

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.


*/

#include<iostream>

#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<bool>primeNums;
vector<int> combined;
//소수
bool prime(int n) {
	if (n == 0 || n == 1)return false;
	for (int i = 2; i < sqrt(n); i++) {
		if (n % i == 0)return false;
	}
	return true;
}

//소수 에라토스테네스의 체
vector<bool> makePrimePool(string numbers) {
	int digit = pow(10, numbers.length());
	vector<bool> primeNum(digit, true);
	fill(primeNum.begin(), primeNum.begin() + 2, false);
	for (int i = 2; i < digit; i++) {
		if (primeNum[i] == false) continue;
		for (int j = i * 2; j < digit; j += i) {
			primeNum[j] = false;
		}
	}
	return primeNum;
}
//순열조합
void permutation(int depth, string numbers, string res, vector < bool>visited) {
	if (depth == numbers.length())
		return;
	for (int i = 0; i < numbers.length(); i++) {
		if (!visited[i]) {
			string currNum = res + numbers[i];
			visited[i] = true;
			if (primeNums[atoi(currNum.c_str())])
			//if (prime(atoi(currNum.c_str())))
				combined.push_back(atoi(currNum.c_str()));
			permutation(depth+ 1, numbers, res + numbers[i], visited);
			visited[i] = false;
		}
	}
}

int solution(string numbers) {	
	vector < bool>visited(numbers.size());
	primeNums = makePrimePool(numbers);

	permutation(0, numbers, "", visited);

	//중복제거
	sort(combined.begin(), combined.end());
	combined.erase(unique(combined.begin(), combined.end()), combined.end());

	for (auto elem : combined) {
		cout << elem << endl;
	}
	
	return combined.size();
}

int main() {
	cout << solution("17");
}