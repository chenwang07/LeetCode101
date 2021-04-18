#include <iostream>
#include <vector>
#include <algorithm> 
#include "algorithmDeclaration.h"

using namespace std;

int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;

    sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b)
    {
        return a[1] < b[1];
    });

    int pre = intervals[0][1];
    int removed = 0;

    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i][0] < pre) {
            removed++;
        }
        else {
            pre = intervals[i][1];
        }
    }
    return removed;
}


/*
    vector<vector<int>> inputData = { {1, 2} ,{2, 4},{1, 3} };
    int totalRemoved = eraseOverlapIntervals(inputData);
    cout << totalRemoved << endl;
*/