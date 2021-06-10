#include<iostream>

using namespace std;


class rgbDistance {
private:
	int houseCnt;
	int r, g, b;
	int ta, tb, tc;
	bool flag;
public:
	int minMax(int a, int b) {
		return a < b ? a : b;
	}

	void answer() {		
		cin >> houseCnt;
		//초기화.
		ta = tb = tc = 0;

		for (int i = 0; i < houseCnt; i++) {
			//값 입력받기.
			cin >> r;
			cin >> g;
			cin >> b;

			//다음에 들어오는 값의 비교.
			r += minMax(tb, tc);
			g += minMax(ta, tc);
			b += minMax(ta, tb);

			//사용할 최솟값 저장.
			ta = r;
			tb = g;
			tc = b;
		}
		// 3가지중 가장 저렴한것 선택.
		cout << minMax(minMax(r, g), b);
	}
};

int main(int argc, char* argv[]) {
	rgbDistance rd;
	rd.answer();
	return 0;


}
