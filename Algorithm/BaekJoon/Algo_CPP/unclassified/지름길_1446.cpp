//https://www.acmicpc.net/problem/1446
#include<iostream>

using namespace std;
struct SED
{
	int start = 0;
	int end = 0;
	int distance = 0;
};
class Answer {
private:
	int N, D;
	SED sed[13];
	int shorest;


public:

	void swap(SED& n1, SED& n2) {
		SED tmp;
		tmp = n1;
		n1 = n2;
		n2 = tmp;
	}
	//버블정렬
	void sort() {
		for (int i = 0; i < N; i++)
			for (int j = i + 1; j < N; j++)
				if (sed[j].start < sed[i].start) {
					swap(sed[j], sed[i]);
				}
	}
	int min(int a, int b) {
		return a <= b ? a : b;
	}
	void input() {
		cin >> N >> D;
			shorest = D;
		for (int i = 0; i < N; i++) {
			SED tmpSed;
			cin >> tmpSed.start >> tmpSed.end >> tmpSed.distance;
			//도착지점을 넘어가거나, 지름길이 더 느릴경우 필요없음.
			if (tmpSed.end > D || tmpSed.end - tmpSed.start < tmpSed.distance) {
				N--, i--;
				continue;
			}
			sed[i] = tmpSed;
		}
		sort();
	}
	void check(int n, int pos, int dist) {
		shorest = min(shorest, min(D - pos + dist, D - sed[n].end + sed[n].distance + dist));
		for (int i = n; i < N; i++) {			
			//뒤돌아가 갈 수 없음으로, 다음 지점의 시작위치가 더 낮을 경우 패스.
			if (sed[n].end > sed[i + 1].start)
				continue;
			//지름길 이용.
			else if (sed[n].end == sed[i + 1].start)
				check(i + 1, sed[n].end, dist + sed[n].distance);
			//다음 지점까지 길에서 중간이 비어 있을 경우
			else {				
				check(i + 1, sed[i + 1].start, dist + min(sed[n].distance + sed[i + 1].start - sed[n].end, sed[i + 1].start - pos));
			}			
		}
	}

	void solution() {
		for (int i = 0; i < N; i++) 
			check(i, sed[i].start, sed[i].start);	
		cout << shorest;
	}
};

int main() {
	cin.tie(NULL); cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	Answer answer;
	answer.input();
	answer.solution();

}