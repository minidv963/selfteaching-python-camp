import re
import collections
import jieba
count = int()


def stast_text_en(text, count):
    ''' 统计英文单词词频出现的次数 '''
    if type(text) == str:
        text1 = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*',' ')  # 清除不必要的字符
        text2 = text1.split()
        print(text2)
        print(collections.Counter(text2).most_common(count))
    else:
        raise ValueError('此文本为非字符串')

def stast_text_cn(text, count):
    ''' 统计中文词频出现的次数 '''
    if type(text) == str:
        text1 = re.findall(r'[\u4e00-\u9FA5]', text)# 提取中文
        text2 = ''.join(text1)
        text3 = jieba.lcut(text2)
        text_list = []
        for i in text3:  # 用for 遍历分词
            if len(i) >= 2:  # 只取长度大于2的词汇
                text_list.append(i)  # 将其添加到列表里
        counts = collections.Counter(text_list).most_common(count)

        return counts

    else:
        raise ValueError('此文本为非字符串')


def stast_text(text, count):
    ''' 统计中文和英文词频出现的次数 '''
    if type(text) == str:
        print(stast_text_en(text, count) + stast_text_cn(text, count))
    else:
        raise ValueError('此文本为非字符串')