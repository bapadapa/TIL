/*
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

class sumOfNums {
private:
	unsigned int  cnt;
	char num[101];
	int sum = 0;
public:
	void answer() {
		cin >>cnt;

		//입력받기.
		for (int i = 0; i < cnt; i++) {
			cin >> num[i];			
			sum += num[i] - '0';			
		}

		cout << sum;
	}
};

int main(int argc, char* argv[]) {
	sumOfNums SON;
	SON.answer();
	return 0;
		
}
