#prepare lexion.txt from Appen lexicon using SAMPA code
import os
appen_lexicon_file = '/data/USE_ASR001/TABLE/LEXICON.TBL'
fid = open(appen_lexicon_file)
all_lines =  fid.readlines()
fid.close()
vowel_diphthon_set = set(['V','A','{','E','E:','3`','I','i','O','U','u','@','@`','aI', 'eI','OI','aU','oU'])
lexicon = []
ph_set = set()
count = 0
print(len(all_lines))
for ln in all_lines[1:]:
    count  = count+1
    temp = ln.strip().split('\t')
    
    for lex_chunk in temp[2:]:
        syls = lex_chunk.strip().split('.')
        for j in range(len(syls)):
            phs= syls[j].strip().split(' ')
            for i in range(len(phs)):
                if phs[i] in vowel_diphthon_set:
                    if '"' in syls[j]:
                        phs[i] = phs[i]+'1'
                    elif '%' in syls[j]:
                        phs[i] = phs[i]+'2'
                    else:
                        phs[i] = phs[i]+'0'
            syls[j] = ' '.join(phs)
        lex = ' '.join(syls).replace('" ','').replace('% ','').replace('. ','').replace('# ','')
        
          
        #lex = lex_chunk.strip().replace('" ','').replace('% ','').replace('. ','')
        new_ln = temp[0].upper()+' '+lex
        if temp[0].upper() == 'AMRO':
            print(new_ln)
        lexicon.append(new_ln)
        for ph in lex.split(' '):
            ph_set.add(ph)
if not os.path.exists('../data/local/dict_nosp'):
    os.mkdir('../data/local/dict_nosp')
fid = open('../data/local/dict_nosp/lexicon.txt','w')
fid.write('!SIL sil\n<UNK> spn\n')
for lex in sorted(set(lexicon)):
    fid.write(lex+'\n')
fid.close()
print (sorted(ph_set))
print(len(ph_set))

fid =open('../data/local/dict_nosp/nonsilence_phones.txt','w')
for ph in sorted(ph_set):
    fid.write(ph+'\n')
fid.close()

