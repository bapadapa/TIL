#include<iostream>

using namespace std;


class rgbDistance {
private:
	int houseCnt;
	// [RGB색수][최대 집의갯수]
	// 입력받은 Cost들
	int rgbC[3][1001] = { 0, };

	// 입력받은 Cost의 합.
	int rgbMemo[3][1001] = { 0, };

	int bestCost;
public:
	void answer() {
		cin >> houseCnt;

		//구할 집 갯수 및 Cost 값 입력.
		for (int i = 0; i < houseCnt; i++) {

			for (int j = 0; j < 3; j++) {
				cin >> rgbC[j][i];
			}
		}
		//배열로 하려고 1뺌.		
		int last = houseCnt - 1;

		//마지막 값을 초기값으로 설정.
		rgbMemo[0][last] = rgbC[0][last];
		rgbMemo[1][last] = rgbC[1][last];
		rgbMemo[2][last] = rgbC[2][last];

		//마지막 값을 저장했기 때문에 1뺴줌.
		last--;

		int tmp, tmp2;
		bool flag;

		for (int i = last; i >= 0; i--) {	
			for (int k = 0; k < 3; k++) {
				bestCost = tmp = tmp2 = 0;
				flag = true;
				for (int j = 0; j < 3; j++) {
					if (k == j)
						continue;
					else if (flag) {
						tmp = rgbMemo[j][i+1];
						flag = false;
					}
					else
						tmp2 = rgbMemo[j][i+1];
					if (tmp != 0 && tmp2 != 0) {						
						bestCost = tmp <= tmp2 ? tmp : tmp2;						
						rgbMemo[k][i] = rgbC[k][i] + bestCost;
					}
				}
			}
		}

		// 가장 위에 저장된 값비교.
		bestCost = rgbMemo[0][0] <= rgbMemo[1][0] ? rgbMemo[0][0] : rgbMemo[1][0];
		bestCost = bestCost <= rgbMemo[2][0] ? bestCost : rgbMemo[2][0];

		cout << bestCost;

	}
};

int main(int argc, char* argv[]) {
	rgbDistance rd;
	rd.answer();
	return 0;


}
