
#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>



std::string minWindow(std::string s, std::string t) {
    int left = 0, right = 0;
    int subStrHead = 0;
    int minSize = s.size() + 1;
    int count = 0;

    std::unordered_map<char, int> patternCount;
    std::unordered_map<char, int> freqCount;

    for (int i = 0; i < t.size(); i++) {
        patternCount[t[i]]++;
        freqCount[t[i]] = 0;
    }

    for (; right < s.size(); right++) {
        if (patternCount.find(s[right]) != patternCount.end()) {
            if (++freqCount[s[right]] == patternCount[s[right]]) count++;
            while (count == patternCount.size()) {
                if (right - left + 1 < minSize) {
                    subStrHead = left;
                    minSize = right - left + 1;
                }
                if (patternCount.find(s[left]) != patternCount.end()) {
                    freqCount[s[left]]--;
                    if (freqCount[s[left]] < patternCount[s[left]]) count--;
                }
                ++left;
            }
        }
    }
    return minSize > s.size() ? "" : s.substr(subStrHead, minSize);
}


/*
    string s = "ADOBECODEBANC";
    string t = "ABC";
    string res = minWindow(s, t);
*/