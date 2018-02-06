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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""


def bangalore_calls():
    # 被(080)呼叫的号码前缀集合
    pre_called_nums = set()
    # 来自班加罗尔的固话总数
    _total_from_bangalore_num = 0
    # 来自班加罗尔且打往班加罗尔的固话总数
    _total_from_bangalore_to_bangalore_num = 0

    for call in calls:
        # 获取主叫号码
        call_num = call[0]
        # 主叫号码前5位，用于判断是否(080)
        pre_call_num = call_num[:5]
        if '(080)' == pre_call_num:
            # 获取被叫号码
            called_num = call[1]
            # 电话来自班加罗尔
            _total_from_bangalore_num += 1
            if called_num.startswith('(080)'):
                # 被叫电话为班加罗尔
                _total_from_bangalore_to_bangalore_num += 1

            if called_num.startswith('('):
                # 如果被叫号码是固定电话，获取区号')'位置
                called_num_index = called_num.find(')')
                if called_num_index != -1:
                    # 将区号加入集合
                    pre_called_nums.add(called_num[:called_num_index + 1])
            elif called_num.startswith('7') \
                    or called_num.startswith('8') \
                    or called_num.startswith('9') \
                    or called_num.startswith('140'):
                # 如果主叫号码以7、8、9、140开头，获取移动前缀
                pre_called_nums.add(called_num[:4])

    print("%.2f%% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
          % ((_total_from_bangalore_to_bangalore_num / _total_from_bangalore_num) * 100))

    # 将集合按题意转为列表，排序并打印
    pre_called_nums = sorted(list(pre_called_nums))
    for pre_called_num in pre_called_nums:
        print(pre_called_num)


bangalore_calls()
