//#include<iostream>
//
//using namespace std;
//1차 시도.

//class goldbachConjecture {
//private:
//	int decimal[2] = { 0, };
//	int enterNum = 8;
//	int num1, num2;
//	bool isPrime = false;
//
//public:
//	void _answer() {
//		//enterNum이 0이 들어오면 종료
//		while (true) {
//
//			cin >> enterNum;
//			if (enterNum == 0)
//				break;
//
//			//홀수값을 원하는 것이니 3부터 시작.
//			num1 = 3;
//			num2 = enterNum - num1;
//
//			// 중간 넘어가기 전까지 반복.
//			while (num1 < num2) {
//				//소수면 탈출
//				if (_isPrime(num1, num2)) {
//					isPrime = true;
//					break;
//				}
//				num1 += 2;
//				num2 -= 2;
//			}
//
//			//출력부			
//			if (isPrime)
//				cout << enterNum << " = " << num1 << " + " << num2 << "\n";
//			else
//				cout << "Goldbach's conjecture is wrong." << "\n";
//			isPrime = false;
//
//
//		}
//
//	}
//	bool prime(int n)
//	{
//		if (n % 2 == 0 && n != 2)
//			return false;
//
//		for (int i = 3; i <= sqrt(n); i += 2)
//		{
//			if (n%i == 0)
//				return false;
//		}
//		return true;
//	}
//
//	//뽑은 숫자가 소수인지 파악.
//	bool _isPrime(int n1, int n2) {
//		bool _isPrime[2] = { true,true };
//		_isPrime[0] = prime(n1);
//		_isPrime[1] = prime(n2);
//		if (_isPrime[0] == true && _isPrime[1] == true)
//			return true;
//		else
//			return false;
//	}
//
//
//};

//2차 시도

//class goldbachConjecture {
//private:
//	int primeNum[1000000] = { 0, };
//	bool _checkPrime[1000000] = { false, };
//	int arrCnt = 0;
//	int _inputNum;
//	int maxPrime;
//	bool _isEnter = true;
//	bool _isgoldbash = true;
//
//public:
//
//
//
//	void  _answer() {
//		_setArr();
//
//
//		while (_isEnter) {
//			cin >> _inputNum;
//
//			for (int i = 0; i < sizeof(primeNum); i++) {
//				if (primeNum[i] > _inputNum) {
//					maxPrime = i;
//					break;
//				}
//			}
//			for (int i = 0; i < maxPrime; i++) {
//				if (primeNum[i] + primeNum[maxPrime - i] == _inputNum)
//					cout << _inputNum << " = " << primeNum[i] << " + " << primeNum[maxPrime - i] << "\n";
//				else
//					cout << "Goldbach's conjecture is wrong." << "\n";
//			}
//		}
//
//
//	}
//
//	void _checkArr() {
//		for (int i = 0; i < sizeof(primeNum); i++) {
//			cout << primeNum[i] << "\n";
//		}
//	}
//
//	void _setArr() {
//		for (int i = 2; i < 1000000; i++) {
//			if (_checkPrime[i] == false) {
//				for(int j = i ; j < 100000)
//
//			}
//		}
//
//
//	
//	}
//
//};
//
//int main(void) {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//
//	goldbachConjecture gc;
//	//gc._setArr();
//	//gc._checkArr();
//		gc._answer();
//
//	return 0;
//}


//bool prime(int n)
//{
//	if (n % 2 == 0 && n != 2)
//		return false;
//
//	for (int i = 3; i <= sqrt(n); i += 2)
//	{
//		if (n%i == 0)
//			return false;
//	}
//	return true;
//
//
//}

//최종 성공
#include<iostream>
#include<math.h>
using namespace std;


class goldbachConjecture {
private:

	bool prime_c[1000001];
	int _enterNum;
	bool check;
public:

	void _answer() {
		//소수 체크.
		_setPrime();
		while (true) {
			cin >> _enterNum;
			check = false;
			if (_enterNum == 0)
				break;
			else if (_enterNum % 2 == 1)
				continue;


			for (int i = 3; i <= _enterNum; i += 2) {
				if (prime_c[i] && prime_c[_enterNum - i]) {
					cout << _enterNum << " = " << i << " + " << _enterNum - i << "\n";
					check = true;
					break;
				}
			}
			if (!check)
				cout << "Goldbach's conjecture is wrong." << "\n";			
		}

	}
	void _setPrime() {
		//초기화.
		for (int i = 2; i < 1000001; i++) {
			prime_c[i] = true;
		}
		
		//소수판별
		for (int i = 2; i < sqrt(1000001); i++) {			
			if (prime_c[i]) {
				for (int j = i+i; j < 1000001; j += i) {
					prime_c[j] = false;
				}
			}
		}

	}
};

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	goldbachConjecture gc;
	gc._answer();

}