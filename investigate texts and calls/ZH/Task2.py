"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import string

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


def longest_time_num():
    """
    以电话号码为键，通话总时长为值的一个字典
    :return:
    """
    longest_nums = {}
    for call in calls:
        # 获取通话时间，转为int类型
        time = int(call[3])
        if call[0] not in longest_nums:
            # 如果去电号码不在字典中，赋值并设置通话时间
            longest_nums[call[0]] = time
        else:
            # 如果去电号码在字典中，更新通话时间
            longest_nums[call[0]] += time

        if call[1] not in longest_nums:
            # 如果接听号码不在字典中，赋值并设置通话时间
            longest_nums[call[1]] = time
        else:
            # 如果接听号码在字典中，更新通话时间
            longest_nums[call[1]] += time

    sorted_longest_nums = zip(longest_nums.values(), longest_nums.keys())
    # 对zip后的列表进行降序排序
    sorted_longest_nums = sorted(sorted_longest_nums, reverse=True)
    # 取第一个号码信息
    longest_num_time = sorted_longest_nums[0]

    return "%s spent the longest time, %d seconds, on the phone during September 2016." % (
        longest_num_time[1], longest_num_time[0])


print(longest_time_num())
