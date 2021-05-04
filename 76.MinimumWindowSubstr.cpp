
#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>



std::string minWindow(std::string s, std::string t) {
    std::unordered_map<char, int> freq;
    for (int i=0; i < s.size(); i++) {
        freq[s[i]]++;
    }
    int i = 1;
    for (; i < 10; i++) {
        std::cout << i << std::endl;
    }
    return s;

}