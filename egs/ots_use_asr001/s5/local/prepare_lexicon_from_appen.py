#prepare lexion.txt from Appen lexicon using SAMPA code
import os
appen_lexicon_file = '/data/USE_ASR001/USE_ASR001/TABLE/LEXICON.TBL'
fid = open(appen_lexicon_file)
all_lines =  fid.readlines()
fid.close()

lexicon = []
ph_set = set()
count = 0
for ln in all_lines[1:]:
    count  = count+1
    temp = ln.strip().split('\t')
    
    for lex_chunk in temp[2:]:
        lex = lex_chunk.strip().replace('" ','').replace('% ','').replace('. ','')
        new_ln = temp[0]+' '+lex
        lexicon.append(new_ln)
        for ph in lex.split(' '):
            ph_set.add(ph)
if not os.path.exists('../data/local/dict'):
    os.mkdir('../data/local/dict')
fid = open('../data/local/dict/lexicon.txt','w')
fid.write('!SIL sil\n<UNK> spn\n')
for lex in lexicon:
    fid.write(lex+'\n')
fid.close()
print (ph_set)
print(len(ph_set))

fid =open('../data/local/dict/nonsilence_phones.txt','w')
for ph in ph_set:
    fid.write(ph+'\n')
fid.close()

