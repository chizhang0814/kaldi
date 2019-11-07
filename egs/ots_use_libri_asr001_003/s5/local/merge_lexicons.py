import os

lexicon_1='../data/local/lm_libri_ots_asr001_asr003/lexicon_asr001.txt'
lexicon_2='../data/local/lm_libri_ots_asr001_asr003/lexicon_asr003.txt'
lexicon_3='../data/local/lm_libri_ots_asr001_asr003/librispeech-lexicon.txt'

lexicon_set = set()
fid= open(lexicon_1)
all_lines = fid.readlines()
fid.close()
for ln in all_lines:
    lexicon_set.add(ln)


fid= open(lexicon_2)
all_lines = fid.readlines()
fid.close()
for ln in all_lines:
    lexicon_set.add(ln)
    
fid= open(lexicon_3)
all_lines = fid.readlines()
fid.close()
for ln in all_lines:
    lexicon_set.add(ln.replace('\t',' '))

fid = open('../data/local/lm_libri_ots_asr001_asr003/librispeech_use_asr001_asr003_lexicon.txt','w')
for ln in sorted(lexicon_set):
    fid.write(ln)
fid.close()

