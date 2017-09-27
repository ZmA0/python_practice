#-*- coding:utf-8 -*-
'''你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
'''
import os
import re
def findword(path):
    if not os.path.isdir(path):
        return
    filelist=os.listdir(path)
    r=re.compile('\b?(\w+)\b?')
    for file in filelist:
        filepath=os.path.join(path,file)
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1]=='.txt':
            with open(filepath) as f:
                data=f.read()
                words=r.findall(data)
                wordsdict=dict()
                for word in words:
                    word = word.lower()
                    if word in ['a','the','a']:
                        continue
                    if word in wordsdict:
                        wordsdict[word.lower()]+=1
                    else:
                        wordsdict[word.lower()]=1
            result=sorted(wordsdict.items(),key=lambda t:t[1],reverse=True)#比较参数为每个词的个数
            print('file:%s->the most important word:%s' % (file,result[0]))

findword('C:/Users/10071/PycharmProjects/py practice/0006_txt')


