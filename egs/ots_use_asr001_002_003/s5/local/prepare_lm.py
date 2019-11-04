import os
appen_lexicon_file = '/data/USE_ASR001/USE_ASR001/TABLE/LEXICON.TBL'
vocab_file='../data/local/lm/vocab.txt'

if not os.path.exists('../data/local/lm'):
    os.mkdir('../data/local/lm')


fid = open(appen_lexicon_file)
all_lines = fid.readlines()
fid.close()

fid = open(vocab_file,'w')
for ln in all_lines:
    fid.write(ln.split('\t')[0]+'\n')
fid.close()


