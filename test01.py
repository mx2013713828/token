‘’’test GitHub’’’
# !/usr/bin/python
# -*- encoding:utf-8 -*-
import jieba
import nltk
import os
import sys
import re
import codecs
reload(sys)
#sys.setdefaultcoding("utf-8")

def stoplist(file):
    stopwords =[line.strip() for line in open(file,'r')]
    return stopwords


def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    sentence_seged = [word for word in list(sentence_seged)]

    stopwords = stoplist('stopwords.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return sentence_seged


input = open('nlp2.txt','r').read()
#print input.read()

#print seg_sentence(input)
print stoplist('stopwords.txt')
for w in seg_sentence(input):
    print w
#outputs.close()
#inputs.close()