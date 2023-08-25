#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "algorithmDeclaration.h"

using namespace std;



vector<int> partitionLabels(string S) {
    unordered_map<char, int> char_freq;
    vector<int> res;

    for (int i = 0; i < S.length(); i++) {
        char c = S[i];
        if (char_freq.find(c) == char_freq.end()) {
            char_freq[c] = 1;
        }
        else {
            char_freq[c]++;
        }
    }

    unordered_map<char, int> current_char;
    int n = 0;
    for (int i = 0; i < S.length(); i++) {
        n++;
        char c = S[i];
        if (current_char.find(c) == current_char.end()) {
            current_char[c] = 1;
        }
        char_freq[c]--;
        if (char_freq[c] == 0) {
            current_char.erase(c);
        }
        if (current_char.size() == 0) {
            res.push_back(n);
            n = 0;
        }
    }
    return res;
 }


/*

string s = "ababcbacadefegdehijhklij";
vector<int> res = partitionLabels(s);

*/