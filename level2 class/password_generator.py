# Use an import statement at the top
import random
import string

word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)


def generate_password():
    random_word_list = random.sample(word_list, 3)
    # join方法要求参数为string，否则回出现异常
    # str(password)将列表元素转为string包装程序正常运行
    return ''.join(str(password) for password in random_word_list)


print(generate_password())

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
