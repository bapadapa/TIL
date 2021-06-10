/*

--출처--
프로그래머스

--문제 제목--
카카오프렌즈 컬러링북

문제 설명
카카오 프렌즈 컬러링북
출판사의 편집자인 어피치는 네오에게 컬러링북에 들어갈 원화를 그려달라고 부탁하여 여러 장의 그림을 받았다.
여러 장의 그림을 난이도 순으로 컬러링북에 넣고 싶었던 어피치는 영역이 많으면 색칠하기가 까다로워 어려워진다는 사실을 발견하고 그림의 난이도를 영역의 수로 정의하였다. (영역이란 상하좌우로 연결된 같은 색상의 공간을 의미한다.)

그림에 몇 개의 영역이 있는지와 가장 큰 영역의 넓이는 얼마인지 계산하는 프로그램을 작성해보자.

위의 그림은 총 12개 영역으로 이루어져 있으며, 가장 넓은 영역은 어피치의 얼굴면으로 넓이는 120이다.

입력 형식
입력은 그림의 크기를 나타내는 m과 n, 그리고 그림을 나타내는 m × n 크기의 2차원 배열 picture로 주어진다.
제한조건은 아래와 같다.
	1 <= m, n <= 100
	picture의 원소는 0 이상 2^31 - 1 이하의 임의의 값이다.
	picture의 원소 중 값이 0인 경우는 색칠하지 않는 영역을 뜻한다.

출력 형식
리턴 타입은 원소가 두 개인 정수 배열이다. 그림에 몇 개의 영역이 있는지와 가장 큰 영역은 몇 칸으로 이루어져 있는지를 리턴한다.

예제 입출력
m	n	picture							answer
6	4	[[1, 1, 1, 0], [1, 2, 2, 0], 	[4, 5]
		[1, 0, 0, 1], [0, 0, 0, 1],
		[0, 0, 0, 3], [0, 0, 0, 3]]
*/

#include<iostream>

#include <vector>

using namespace std;

int checkColor(int color , pair<int, int> dim, int x, int y, vector<vector<int>> &picture) {
	int sum = 1;
	// 범위가 넘어갈 수 있기때문에 color체크는 맨뒤로..
	if ( x >= dim.first || y >= dim.second || x <0 || y < 0 || picture[x][y] != color )
		return 0;

	else {
		picture[x][y] = 0;

		sum += checkColor(color, dim, x+1, y, picture);
		sum += checkColor(color, dim, x, y + 1, picture);
		sum += checkColor(color, dim, x - 1, y, picture);		
		sum += checkColor(color, dim, x, y-1, picture);
	}
	return sum;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int number_of_area = 0;
	int max_size_of_one_area = 0;

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (picture[i][j] == 0)
				continue;
			else {
				int sum = checkColor(picture[i][j], make_pair(m,n), i, j, picture);
				number_of_area++;
				if (sum > max_size_of_one_area)
					max_size_of_one_area = sum;
			}
		}
	}

	vector<int> answer(2);
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}