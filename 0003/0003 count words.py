# -*- coding:utf-8 -*-
'''
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
import re
fin=open('words.txt','r')
content=fin.read()
r=re.compile('\b?(\w+)\b?')
words=r.findall(content)
worddict=dict()
for word in words:
    if word.lower() in worddict:
        worddict[word.lower()]+=1#count the numbers
    else:
        worddict[word]=1#if not exist,add
for key,value in worddict.items():
    print ('%s:%s' % (key,value))#both the words and numbers