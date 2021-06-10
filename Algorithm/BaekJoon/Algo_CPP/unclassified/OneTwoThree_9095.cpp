//백준
//정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.합을 나타낼 때는 수를 1개 이상 사용해야 한다.
//정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
//첫째 줄에 테스트 케이스의 개수 T가 주어진다.각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.n은 양수이며 11보다 작다.

#include <iostream>
using namespace std;
class oneTwoThree {
private:
	int sumArr[11] = { 0, };
	int n;
public:
	void _setNum() {
		cin >> n;
		//규칙이 3번째부터 생김.
		sumArr[0] = 1;
		sumArr[1] = 2;
		sumArr[2] = 4;
	}

	void _answer() {
		for (int i = 3; i < 11; i++) {
			sumArr[i] = sumArr[i - 1] + sumArr[i - 2] + sumArr[i - 3];
		}
	}
	void _print() {
		cout << sumArr[n - 1] << endl;
	}
};

int main(void)
{
	oneTwoThree sc;
	int testCase;
	cin >> testCase;

	for (int i = 0; i < testCase; i++) {
		sc._setNum();
		sc._answer();
		sc._print();
	}
	return 0;
}



//#include <iostream>
//#include<cstring>
//using namespace std;
//
//
//class sumCount {
//private:
//	int sumArr[11];
//	int sumCnt[11] = { 0, };
//	int n;
//public:
//	void _setNum() {
//		cin >> n;
//		//규칙이 3번째부터 생김.
//		memset(sumCnt, 0, sizeof(sumCnt));
//		sumCnt[0] = 1;
//		sumCnt[1] = 2;
//		sumCnt[2] = 4;
//	}
//
//	void _answer() {
//			for (int i = 3; i < 11; i++) {
//				for (int j = 1; j <= (i + 1); j += 2) {
//					//마지막 카운트
//					if ((i+1) - j < 1) {
//						sumCnt[i] += 1;
//						break;
//					}
//					sumCnt[i] += (i + 1) - j;
//				}
//				sumCnt[i] += (1 + (i + 1) - 3 + sumCnt[i - 3]);
//			}
//	}
//	void _print() {
//		cout << sumCnt[n - 1] <<endl;
//	}
//};
//
//int main(void)
//{
//	sumCount sc;
//	int testCase;
//	cin >> testCase;
//
//	for (int i = 0; i < testCase; i++) {
//		sc._setNum();
//		sc._answer();
//		sc._print();
//	}
//	return 0;
//}
//
//
