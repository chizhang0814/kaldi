import os
import glob

librispeech_root='/data/LibriSpeech-asr-corpus-SLR12/LibriSpeech'
all_lines = glob.glob(librispeech_root+'/*/*/*/*.trans.txt')
fid_w  = open('../data/local/lm/librispeech_corpus.txt','w')
for trans in all_lines:
    fid = open(trans)
    all_texts = fid.readlines()
    fid.close()

    for ln in all_texts:
        fid_w.write((' '.join(ln.strip().split(' ')[1:]))+'\n')

fid_w.close()
