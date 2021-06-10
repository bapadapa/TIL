#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<bool> primeNum(n + 1);
    for (int i = 2; i <= n; i++) {
        if (primeNum[i] == false)
            answer++;

        for (int j = i; j <= n; j += i)
            primeNum[j] = true;
    }

    //시간초과
    /*
    vector<int> primeNum(n+1);
    for (int i = 0; i < primeNum.size(); i++) {
        primeNum[i] = i;
    }
    for (int i = 2; i < primeNum.size(); i++) {
        for (int j = i+1; j < primeNum.size(); j++) {
            if (primeNum[j] % primeNum[i] == 0)
                primeNum.erase(primeNum.begin() + j--);
        }

    }
    answer = primeNum.size() - 2;*/


    return answer;
}