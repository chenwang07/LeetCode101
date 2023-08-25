#include <iostream>
#include <vector>
#include <algorithm>
#include "algorithmDeclaration.h"


int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;

    int arrows = 1;

    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    });

    int start = points[0][0], end = points[0][1];

    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] <= end) {
            start = max(start, points[i][0]);
            end = min(end, points[i][1]);
        }
        else {
            start = points[i][0];
            end = points[i][1];
            arrows++;
        }

    }

    return arrows;
}