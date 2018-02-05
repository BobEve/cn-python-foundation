"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def print_first_text():
    """如果短信数据大于0，则获取第一条数据"""
    if len(texts) > 0:
        first_texts = texts[0]
        print("First record of texts, {} texts {} at time {}".format(first_texts[0], first_texts[1], first_texts[2]))


def print_first_call():
    """如果电话数据大于0，则获取第一条数据"""
    if len(calls) > 0:
        first_calls = calls[0]
        print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(first_calls[0], first_calls[1],
                                                                                        first_calls[2], first_calls[3]))


print_first_text()
print_first_call()
