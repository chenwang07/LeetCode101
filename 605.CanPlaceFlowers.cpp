#include <iostream>
#include <vector>
#include <algorithm>
#include "algorithmDeclaration.h"

using namespace std;

bool canPlaceFlowers(vector<int>& flowerbed, int n) {

	if (n == 0) return true;

	for (int i = 0; i < flowerbed.size(); i++) {
		if (flowerbed[i] == 0) {
			if (i == 0) {
				if (flowerbed.size() == 1 || flowerbed[i + 1] == 0) {
					flowerbed[i] = 1;
					n--;
				}
			}
			else if (i == flowerbed.size()-1){
				if (flowerbed[i - 1] == 0) {
					flowerbed[i] = 1;
					n--;
				}
			}
			else {
				if (flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0) {
					flowerbed[i] = 1;
					n--;
				}
			}
		}

		if (n == 0) break;
	}

	return (n==0) ? true : false;
}

/*

注意flowerbed = {0} 的情况，往后看元素容易越界，需要另外处理
int n = 1;
vector<int> flowerbed = { 0 };
cout << canPlaceFlowers(flowerbed, n) << endl;

*/