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
    longest_nums_dict = {}
    for call in calls:
        # 获取通话时间，转为int类型
        time = int(call[3])
        if call[0] not in longest_nums_dict:
            # 如果去电号码不在字典中，赋值并设置通话时间
            longest_nums_dict[call[0]] = time
        else:
            # 如果去电号码在字典中，更新通话时间
            longest_nums_dict[call[0]] += time

        if call[1] not in longest_nums_dict:
            # 如果接听号码不在字典中，赋值并设置通话时间
            longest_nums_dict[call[1]] = time
        else:
            # 如果接听号码在字典中，更新通话时间
            longest_nums_dict[call[1]] += time

    """
    思路参考：https://stackoverflow.com/questions/31506694/python-dict-more-than-one-max-value
    """
    # 获取通话时间最大值
    longest_times = max(longest_nums_dict.values())
    # 返回所有通话时间最大值对应的电话号码集合，处理重复value的问题
    longest_nums = [k for k, v in longest_nums_dict.items() if v == longest_times]

    # 遍历最大通话时间对应的电话号码集合，输出最大通话时间和电话号码
    for longest_num in longest_nums:
        print("%s spent the longest time, %d seconds, on the phone during September 2016." % (
            longest_num, longest_nums_dict.get(longest_num)))

    # longest_num_time = max(longest_nums_dict.items(), key=lambda x: x[1])
    # return "%s spent the longest time, %d seconds, on the phone during September 2016." % (
    #     longest_num_time[0], longest_num_time[1])


longest_time_num()
# print(longest_time_num())
