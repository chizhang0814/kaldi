import os
Vowels = ['AH0', 'AH1', 'AH2', 
        'AA0','AA1','AA2',
        'AE0','AE1', 'AE2',
        'EH0','EH1','EH2',
        'ER0','ER1','ER2',
        'IH0','IH1','IH2',
        'IY0','IY1','IY2',
        'AO0','AO1','AO2',
        'UH0','UH1','UH2',
        'UW0','UW1','UW2',
        'AY0','AY1','AY2',
        'EY0','EY1','EY2',
        'OY0','OY1','OY2',
        'AW0','AW1','AW2',
        'OW0','OW1','OW2']


librispeech_lexicon = '/home/ubuntu/src/kaldi/egs/ots_use_asr001/s5/local/librispeech-lexicon.txt'
fid  = open(librispeech_lexicon)
all_lexicon = fid.readlines()
fid.close()

for ln in all_lexicon:
    temp = ln.split('\t')
    temp2= ln.split(' ')
    print(temp[0])
    print(temp)
    print(temp[1])
    print('\n')        

