#include<iostream>
using namespace std;

class oneNum {
private:
	int enterNum;
	int oneNumCnt;
	bool _isOneNum = false;

public:
	void _answer() {
		//값 입력받기.
		cin >> enterNum;
		//등차로 이루어진 수의 갯수
		oneNumCnt = 0;
		//1부터 입력받은 값까지 확인.
		for (int i = 1; i <= enterNum; i++) {
			//만약 그 값이 등차면 true
			if (_checkOneNum(i))
				oneNumCnt++;
		}
		//등차로 이루어진 수의 갯수 출력.
		cout << oneNumCnt;
	}

	//검사.
	bool _checkOneNum(int num) {
		//최대 1000이기 때문에 4자리.
		int tmpArr[4] = { 0, };
		_isOneNum = false;

		int cnt = 0;//입력받은 값의 자릿수
		int tmp = num;
		int tmpNum = 0;

		//등차    1번째 자릿수   2번쨰 자릿수
		int ac = num % 10 - (num / 10) % 10;

		// 10이하의 숫자는 무조껀 등차.
		if (tmp < 10) {
			return true;
		}
		
		//배열에 각 자릿수 값 삽입.
		while (tmp > 0) {
			tmpArr[tmpNum++] = tmp % 10;
			tmp /= 10;
			cnt++;
		}
		//배열은 0 부터 시작하기 때문에 0부터 시작.
		for (int i = 0; i < cnt; i++) {
			//마지막 자릿수가 아니라면.
			if (i != cnt - 1) {
				if ((tmpArr[i] - tmpArr[i + 1]) == ac)
					_isOneNum = true;
				else
					_isOneNum = false;
			}
			//마지막 자릿수.
			else if (i == cnt - 1) {
				if ((tmpArr[i - 1] - tmpArr[i]) == ac)
					_isOneNum = true;
				else
					_isOneNum = false;
			}
		}
		return _isOneNum;
	}

};

int main(void) {
	oneNum on;
	on._answer();

	return 0;
}