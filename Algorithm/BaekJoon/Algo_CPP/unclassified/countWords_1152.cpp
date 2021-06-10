
/*
문제
영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.

출력
첫째 줄에 단어의 개수를 출력한다.

예제 입력 1
The Curious Case of Benjamin Button
예제 출력 1
6

예제 입력 2
 Mazatneunde Wae Teullyeoyo
예제 출력 2
3
예제 입력 3
Teullinika Teullyeotzi
예제 출력 3
2
*/
#include<iostream>
#include<string.h>
using namespace std;

class countWords {
private:
	char str[1000001];
	int cnt = 0;	
	int blank = 0;
public:

	void answer() {
		fgets(str, sizeof(str), stdin);

		for (int i = 0; i < sizeof(str); i++) {
			//공백이면 예외
			if (str[i] == ' ' || str[i] == '\0' || str[i] == '\n'){
				blank++;
				continue;
			}
			if (blank > 1)
				break;
			
			//현재 배열에 들어있는 값이 공백이 아니고, 다음 배열에 삽입된 것이 공백이라면
			if ((str[i] != ' ' || str[i] != '\0' || str[i] != '\n') && (str[i + 1] == ' ' || str[i + 1] == '\0' || str[i+1] == '\n')) {
				cnt++;
				blank = 0;
			}
		}
		cout << cnt;
	}

};

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	countWords sW;
	sW.answer();
	return 0;
}