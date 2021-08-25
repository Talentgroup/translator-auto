import time
from GoogleTranslator import GoogleTranslator
from lk_utils.toolbox import *


def readFile(fileName):
    with open(fileName, 'r') as f:
        paragraph = ''
        for line in f.readlines():
            print(line)
            # if line.replace('\n','')!='\n':
            if line[0] != '\n':
                paragraph = paragraph + line
                # paragraph += line.strip('\n')
            else:
                if len(paragraph) > 0:
                    yield paragraph
                    paragraph = ''
        if len(paragraph) > 0:
            yield paragraph


def main():
    translator = GoogleTranslator()
    count = 0
    with open('out.txt', 'a', encoding='utf-8-sig') as df:
        for line in readFile('in.txt'):
            # print(line)
            lk.loga(line)
            if len(line) > 1:
                count += 1
                print('\r' + str(count), end='', flush=True)
                # df.write(line.strip() + "\n")
                result = translator.translate(line)
                # print(result)
                df.write(result.strip() + '\n')


if __name__ == "__main__":
    startTime = time.time()
    main()
    print('%.2f seconds' % (time.time() - startTime))
