#include <iostream>
#include<unordered_map>

#include<string>
#include<vector>
using namespace std;

int solution(string s) {
	vector<char> s2;
	for (int i = 0; i < s.length(); i++) {
		if (s2.empty() || s2.back() != s.at(i))
			s2.push_back(s.at(i));
		else if (s2.back() == s.at(i))
			s2.pop_back();
	}
	return s2.size() ? 0 : 1;
}



//int solution(string s) {
//	int length = s.length();
//	int pos = 0;
//	//È¦¼ö Ã¼Å©
//	unordered_map<char, int> check;
//	for (int i = 0; i < length; i++) {
//		unordered_map<char,int>::iterator itr = check.find(s.at(i));
//		if (itr == check.end()) {
//			check.insert(unordered_map<char, int>::value_type(s.at(i), 1));
//		}
//		else {
//			itr->second++;
//		}
//	}
//	for (auto elem : check) {		
//		if (elem.second % 2)
//			return 0;
//	}
//	
//	while (pos < length - 1) {
//		if (s.at(pos) == s.at(pos + 1)) {
//			s.erase(pos, 2);
//			length -= 2;
//			if (pos) pos--;
//			continue;
//		}
//		pos++;
//	}
//	return s.length() ? 0 : 1;
//}

int main() {
	cout << solution("cdcd");
}