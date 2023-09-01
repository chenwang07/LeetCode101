


test_case_1 = [-10]
test_case_2 = []
test_case_3 = [2,4,6,8,10]
test_case_4 = [-2,-4,-6,-8,-10]

test_cases = [test_case_1,test_case_2, test_case_3, test_case_4]
ans = [-10, None, 8, -4]


def find_second_max(n):
    if not n: return None
    if len(n) < 2: return n[0] 
    max_ = float("-inf")
    second_ = float("-inf")

    for i in n:
        if i >= max_:
            second_ = max_
            max_ = i
        elif i >= second_:
            second_ = i
        else:
            pass
    return second_

for test_case, correct_ans in zip(test_cases, ans):
    try:
        res = find_second_max(test_case)
        assert(res == correct_ans)
    except AssertionError:
        print(f"Test faild for {test_case}, result is {res}, should be {correct_ans}")
    else:
        print(f"Test succeed for {test_case}, result is {res}, should be {correct_ans}")
