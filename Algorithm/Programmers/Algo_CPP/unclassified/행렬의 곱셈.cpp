//https://programmers.co.kr/learn/courses/30/lessons/12949

#include <iostream>
#include <string>
#include <vector>

using namespace std;


vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;        
    int resultCal = arr1.size();
    int resultRow = arr2.at(0).size();
    int mulTime = arr1.at(0).size();

    for (int i = 0; i < resultCal; i++) {
        vector<int> tmpVec;
        for (int j = 0; j < resultRow; j++) {
            int tmp = 0;
            for (int k = 0; k < mulTime; k++) {                
                tmp += arr1.at(i).at(k) * arr2.at(k).at(j);
            }
            tmpVec.push_back(tmp);
        }
        answer.push_back(tmpVec);
    }
    return answer;
}

int main() {
    vector<vector<int>> arr1{ {1,2,3} ,{4,5,6} };
    vector<vector<int>> arr2{ {1,4},{2,5},{3,6} };

    for (auto elem : solution(arr1, arr2)) {
        for (auto num : elem) {
            cout << num << " ";
        }
        cout << endl;
    }
    
}