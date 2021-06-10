//https://programmers.co.kr/learn/courses/30/lessons/42578
#include<iostream>


#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;


bool cmp(const vector<string> &first, vector<string> & second) {
	return first.back() > second.back();
}
//Map이용 안함.
int solution(vector<vector<string>> clothes) {
	int answer = 1;
	sort(clothes.begin(), clothes.end(), &cmp);
	vector<int> cnt;
	int pos = 0;
	string tmp = clothes.at(0).back();
	for (auto elem : clothes) {
		if (cnt.empty()) {
			cnt.push_back(2);

		}
		else if (tmp != elem.back()) {
			tmp = elem.back();
			cnt.push_back(2);
			pos++;
		}
		else 
			cnt.at(pos)++;
	}
	for (auto elem : cnt) {
		answer *= elem;
	}
		return answer-1;

}

//Map이용
int solution2(vector<vector<string>> clothes) {
	int answer = 1;
	unordered_map <string, int> hClothes;	
	for (auto elem : clothes) {
		auto itr = hClothes.find(elem.back());
		if (itr == hClothes.end()) {
			hClothes.insert(unordered_map<string, int>::value_type ( elem.back(), 2));
		}
		else {
			itr->second++;
		}
	}
	for (auto elem : hClothes) {		
		answer *= elem.second ;
	}	
	return answer -1 ;
}



int main() {
	cout << solution({ {"yellow_hat", "f"},{"blue_sunglasses", "f"},{"green_turban", "f"} });


}
