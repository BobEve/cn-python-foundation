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

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""


def get_call_nums():
    # 所有主叫号码集合
    call_nums = set()
    for call in calls:
        call_nums.add(call[0])

    return call_nums


def check_call_nums(call_nums):
    """检查所有主叫号码列表，遍历被叫、发信息、收信息号码，
    然后将其由所有主叫码号列表移除
    """
    for call in calls:
        # 被叫号码
        called = call[1]
        if called in call_nums:
            # 如果被叫号码在主叫号码列表，将其移除
            call_nums.remove(called)

    for text_call in texts:
        # 发短信号码
        call = text_call[0]
        # 收短信号码
        called = text_call[1]
        if call in call_nums:
            # 如果发短信号码在主叫号码列表，将其移除
            call_nums.remove(call)
        if called in call_nums:
            # 如果收短信号码在主叫号码列表，将其移除
            call_nums.remove(called)

    # 将集合按题意转为列表，排序并打印
    call_nums = sorted(list(call_nums))
    print("These numbers could be telemarketers: ")
    for call_num in call_nums:
        print(call_num)


check_call_nums(get_call_nums())
