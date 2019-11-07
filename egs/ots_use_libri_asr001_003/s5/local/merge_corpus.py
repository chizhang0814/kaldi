import os

corpus_1 = '../data/local/lm_libri_ots_asr001_asr003/corpus_libri_asr001.txt'
corpus_2 = '../data/local/lm_libri_ots_asr001_asr003/corpus_asr003.txt'

corpus = set()

fid = open(corpus_1)
all_lines = fid.readlines()
fid.close()
for ln in all_lines:
    corpus.add(ln)

fid = open(corpus_2)
all_lines = fid.readlines()
fid.close()

for ln in all_lines:
    corpus.add(ln)

fid = open('../data/local/lm_libri_ots_asr001_asr003/corpus_libri_asr001_asr003.txt','w')
for ln in sorted(corpus):
    fid.write(ln)
fid.close()

