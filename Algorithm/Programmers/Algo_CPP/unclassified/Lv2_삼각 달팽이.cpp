/*
--출처--
프로그래머스

--문제 제목--
삼각 달팽이
문제 설명
정수 n이 매개변수로 주어집니다.
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.


제한사항
n은 1 이상 1,000 이하입니다.

입출력 예
n	result
4	[1, 2, 9, 3,10, 8, 4, 5, 6, 7]

5	[1, 2,12, 3,13,11, 4,14,15,10, 5, 6, 7, 8, 9]

6	[1, 2,15, 3,16,14, 4,17,21,13, 5,18,19,20,12, 6, 7, 8, 9,10,11]
*/
#include <iostream>

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
	vector<int> answer;
	vector < vector<int> > tempNum;
	tempNum.resize(n, vector<int>(n, 0));
	int cnt = 1;
	int xPos, yPos;
	xPos = yPos = 0;	

	//우선 배치하기
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {		
			if(i%3 == 0)
				tempNum[xPos++][yPos] = cnt++;
			else if (i % 3 == 1) 
				tempNum[xPos][yPos++] = cnt++;			
			else 
				tempNum[xPos--][yPos--] = cnt++;
		}
		if (i % 3 == 0) {
			xPos--; yPos++;
		}			
		else if (i % 3 == 1) {
			xPos--; yPos-=2;
		}
		else {
			xPos+=2; yPos++;
		}		
	}
	//배치후 입력하기
	for (auto elem : tempNum) {
		for (auto num : elem) {
			if (num == 0)
				break;
			answer.push_back(num);
		}
	}

	return answer;
}
