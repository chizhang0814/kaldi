import os


librispeech_corpus  = '../data/local/lm/librispeech_corpus.txt'
ots_use_asr001_corpus = '../data/local/lm/ots_use_asr001_corpus.txt'

corpus = []

fid = open(librispeech_corpus)
all_lines = fid.readlines()
fid.close()

corpus = all_lines

fid = open(ots_use_asr001_corpus)
ots_lines = fid.readlines()
fid.close()

for ln in ots_lines:
    corpus.append(ln)

fid = open('../data/local/lm/librispeech_ots_use_asr001_corpus.txt','w')
for ln in sorted(set(corpus)):
    fid.write(ln)
fid.close()

