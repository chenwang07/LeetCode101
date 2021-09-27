from collections import defaultdict

def findSubstring(s, words):
    ans = []
    n = len(s)
    cnt = len(words)
    word_len = len(words[0])
    word_dict = defaultdict(int)

    for w in words:    word_dict[w] += 1

    for i in range(word_len):
        left = i
        curr_cnt = 0
        temp_word_dict = defaultdict(int)
        for j in range(i, n-word_len+1, word_len):
            sub_str = s[j:j+word_len]
            if sub_str in word_dict:
                temp_word_dict[sub_str] += 1
                if temp_word_dict[sub_str] <= word_dict[sub_str]:
                    curr_cnt += 1
                else:
                    while temp_word_dict[sub_str] > word_dict[sub_str]:
                        sub_str_2 = s[left: left+word_len]
                        temp_word_dict[sub_str_2] -= 1
                        


                        left += word_len
                if cnt == curr_cnt:
                    ans.append(left)
                    temp_word_dict[s[left:left+word_len]] -= 1
                    curr_cnt -= 1
                    left += word_len
            else:
                temp_word_dict.clear()
                curr_cnt = 0
                left = j + word_len
    return ans


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

res = findSubstring(s, words)
print(1)