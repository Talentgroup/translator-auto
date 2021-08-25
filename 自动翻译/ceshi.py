from pygtrans import Translate
from lk_utils.toolbox import *
import re
import time


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 " \
             "Safari/537.36"
client = Translate()
# client.session.headers['User-Agent'] ==
# 检测语言
# text = client.detect('Answer the question.')
# assert text.language == 'en'

# 翻译句子
# text = client.translate('Look at these pictures and answer the questions.')
# assert text.translatedText == '看这些图片，回答问题。'

# 批量翻译


def tean():

    datas = read_and_write.read_file_by_line('in.txt')
    for data in datas:
        if data + '\n' not in open('mark.txt', 'r', encoding='utf-8').readlines():
            # if data == '':
            #     continue
            texts = client.translate(data)
            # print(texts)
            result = texts.translatedText
            lk.loga(data, result)
            # of = open('out.txt', 'a', encoding='utf-8')
            # of.write(data + ';=;' + result)
            # of.write('\n')
            # of.close()
            # with open('mark.txt', 'a', encoding='utf-8') as f:
            #     f.write(data + '\n')
            #     f.close()
            # # print(result)
            # # except Exception as e:
            # #     print(e)
            # #     print("requests speed so high,need sleep!")
            # #     time.sleep(5)
            # #     print("continue...")
            # #     continue


def creat_dict():
    out = dict()
    datas = read_and_write.read_file_by_line('out.txt')
    for data in datas:
        lk.loga(data)
        key_word = data.split(';=;')[0]
        value = data.split(';=;')[-1]
        out[key_word] = value
    read_and_write.write_json(out, '翻译对照表.json')


if __name__ == '__main__':
    tean()
    # creat_dict()