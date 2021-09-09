#pragma once
#include <vector>
#include <string>

using namespace std;

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// Leetcode 435
int eraseOverlapIntervals(vector<vector<int>>& intervals);
// Leetcode 605
bool canPlaceFlowers(vector<int>& flowerbed, int n);
// Leetcode 452
int findMinArrowShots(vector<vector<int>>& points);
// Leetcode 763
vector<int> partitionLabels(string S);
// Leetcode 122
int maxProfit(vector<int>& prices);
// Leetcode 76
string minWindow(string s, string t);
// Leetcode 104
int maxDepth(TreeNode* root);




