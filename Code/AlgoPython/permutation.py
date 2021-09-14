import itertools


def permute(nums):
    queue = [[i] for i in nums]
    while len(queue[0]) != len(nums):
        head = queue.pop(0)
        for n in nums:
            if n not in head:
                # 这里不能用append, append没有返回值，head + [n]返回新的list给queue.append()函数
                queue.append(head + [n])

    return queue




nums = [1,2,3]

print(permute(nums))
# list of tuples
print(list(itertools.permutations(nums)))

