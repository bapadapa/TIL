/*
--출처--
프로그래머스

--문제 제목--
최대공약수와 최소공배수

--문제 설명--
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

--제한 사항--
두 수는 1이상 1000000이하의 자연수입니다.

--입출력 예--
n	m	return
3	12	[3, 12]
2	5	[1, 10]
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b) {
	return b ?  gcd(b, a % b) : a;
}
vector<int> solution(int n, int m) {
	vector <int> answer;
	answer.push_back(gcd(n, m));
	answer.push_back(n * m / gcd(n, m));

	for (auto elem : answer) {
		cout << elem << endl;
	}
	return answer;
}

int main() {
	solution(1000000, 1000000-1);
}






//아래 왜 안 되는지 모르겠음 ..
/*



vector<int> commonFactor(int num) {

	vector<int> Factor;
	vector<int> _commonFactor;
	for (int i = 1; i <= num; i++) {
		Factor.push_back(i);
	}

	for (auto elem : Factor) {
		if (num % elem == 0)
			_commonFactor.push_back(elem);
	}
	return _commonFactor;
}

vector<__int64> solution(int n, int m) {
	vector <__int64> answer;
	vector<int> commonFactorN;
	vector<int> commonFactorM;

	bool find = false;
	//공약수
	commonFactorN = commonFactor(n);
	commonFactorM = commonFactor(m);

	for (int i = commonFactorN.size()-1; i >= 0; i--) {
		for (int j = commonFactorM.size()-1; j >= 0; j--) {
			if (commonFactorN[i] == commonFactorM[j]) {				
				find = true;
				break;
			}
			else if (commonFactorN[i] > commonFactorM[j])
				break;

		}
		if (find) {
			answer.push_back(commonFactorN[i]);
			break;
		}
			
	}


	__int64 n64 = n;
	__int64 m64 = m;

	//공배수
	if (n < m)
		if (m % n == 0)
			answer.push_back(m);			
		else {
			answer.push_back(n64 * m64);
		}
			
	else
		if (m % n == 0)
			answer.push_back(n);
		else {
			answer.push_back(n64 * m64);
		}
			



	for (auto elem: answer) {
		cout << elem << endl; 
	}

	return answer;
}

int main() {
	
	solution(1000000, 1000000-1);
	cout << 1000000 * (1000000 - 1);
}
*/