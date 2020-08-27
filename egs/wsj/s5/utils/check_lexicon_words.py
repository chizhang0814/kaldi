import os

small_lexicon = '/data3/ots_uke_asr001/s5/data/local/lm/lexicon_uke_asr001.txt'
large_lexicon = '/data3/ots_uke_asr001/s5/data/local/lm/lexicon_libri_use_asr001_asr003.txt'

small = open(small_lexicon).readlines()
large = open(large_lexicon).readlines()

small_words = []
for ln in small:
    word = ln.split('\t')[0]
    #print(word)
    small_words.append(word)

large_words = []
for ln in large:
    word = ln.split(' ')[0]
    #print(word)
    large_words.append(word)

missing_words=[]
for wd in small_words:
    if wd not in large_words:
        missing_words.append(wd)
print(len(missing_words))
'''
for ln in small:
    wd = ln.split('\t')[0]
    if wd in missing_words:
        print(ln)
'''
