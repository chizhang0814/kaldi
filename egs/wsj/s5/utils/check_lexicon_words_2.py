import os

lexicon_file = '/data3/ots_uke_asr001/s5/data/local/lm/lexicon_libri_use_asr001_asr003_beep_uke_asr001_voxforge_nosyl.txt'
wd_set_file = '/data3/ots_uke_asr001/s5/data/local/lm/wd_list_appen_meeting_1_2.txt'

lex_all_lines = open(lexicon_file).readlines()
wd_all_lines = open(wd_set_file).readlines()

wd_set = set()
for ln in wd_all_lines:
    word = ln.strip()
    wd_set.add(word)

lex_words = []
for ln in lex_all_lines:
    word = ln.split(' ')[0]
    #print(word)
    lex_words.append(word)

missing_words=[]
for wd in wd_set:
    if wd not in lex_words:
            missing_words.append(wd)
            
print(missing_words)

