import functools
import collections
import heapq

students = ["a", "b", "a", "c", "a", "b", "c", "b", "a", "b", "c", "c"]
scores = [100,87,88,45,98,45,78,12,88,45,11,65]

def compute_top_k_variance(students, scores, k):

    all_scores = collections.defaultdict(list)

    for student, score in zip(students, scores):
        all_scores[student].append(score)

    top_k_scores = {student: heapq.nlargest(k, scores) for student, scores in all_scores.items() if len(scores) >= k}

    def variance_cal(variance, score):
        return variance + (score-mean)**2

    #test_ans = functools.reduce(variance_cal, scores)

    #ans = {student: functools.reduce(lambda variance, score: variance + (score - mean)**2, scores, 0) for student, scores, mean in aa}

    ans = {student: functools.reduce(lambda variance, score: (variance + (score-mean)**2)/k, scores, 0)\
           for student, scores, mean in ((student, scores, sum(scores)/ k) \
           for student, scores in top_k_scores.items())}


    return ans

variance = compute_top_k_variance(students, scores, 3)
print(variance)