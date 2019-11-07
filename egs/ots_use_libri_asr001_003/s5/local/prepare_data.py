import os
import math
import random

text_file = '../data/use_asr003/text'
fid = open(text_file)
all_lines = fid.readlines()
fid.close()


utt2spk_set = set()
spk2gender_set = set()
for ln in all_lines:
    tmp = ln.strip().split(' ')
    utt_id = tmp[0]
    spk_id = utt_id.split('spkr')[0]+'spkr'+utt_id.split('spkr')[1][0]
    gender = spk_id[0].lower()
    if gender in ['f','m']:
        utt2spk_set.add(utt_id+' '+spk_id+'\n')
        #fid1.write(utt_id+' '+spk_id+'\n')
        spk2gender_set.add(spk_id+' '+gender+'\n')
        #fid2.write(spk_id+' '+gender+'\n')
fid1 = open('utt2spk','w')
for ln in sorted(utt2spk_set):
    fid1.write(ln)
fid1.close()
fid2 = open('spk2gender','w')
for ln in sorted(spk2gender_set):
    fid2.write(ln)
fid2.close()

segment_file = '../data/use_asr003/segments'
fid= open(segment_file)
all_lines = fid.readlines()
fid.close()

#fid3 = open('wav.scp','w')
audio_set = set()

audio_root = '/data2/USE_ASR003/AUDIO'
for ln in all_lines:
    if 'None' in ln:
        continue
    tmp = ln.strip().split(' ')
    recording_id = tmp[1]
    recording_file = audio_root+'/'+recording_id.split('_')[0]+'/'+recording_id+'.wav'
                    
    if not os.path.exists(recording_file):
        print(recording_file)
    audio_set.add(recording_id+' '+recording_file+'\n')
    #fid3.write(recording_id+' '+recording_file+'\n')
                                                
#fid3.close()


print(len(audio_set))
dev_len = int(math.floor(0.1*(len(audio_set)-1)))
tst_len = int(math.floor(0.1*(len(audio_set)-1)))
print(dev_len)
print(tst_len)

dev_lines = set()
dev_audio_set = set()
tst_lines = set()
tst_audio_set = set()
trn_lines = set()
trn_audio_set = set()

audio_set = list(audio_set)
# Randomly select files to add into dev set and test set
for i in range(dev_len):
    idx = random.randint(1, len(audio_set)-1)   
    while ((audio_set[idx] in dev_lines) or (audio_set[idx] in tst_lines)):
        idx = random.randint(1, len(audio_set)-1)
    dev_lines.add(audio_set[idx])
    dev_audio_set.add(audio_set[idx].split(' ')[0])
                            
for i in range(tst_len):
    idx = random.randint(1,len(audio_set)-1)
    while((audio_set[idx] in dev_lines) or (audio_set[idx] in tst_lines)):
        idx = random.randint(1, len(audio_set)-1)
    tst_lines.add(audio_set[idx])
    tst_audio_set.add(audio_set[idx].split(' ')[0])
# add rest lines into train set
for ln in audio_set: # skip the first line, which are the column names
    if ((ln in dev_lines) or (ln in tst_lines)):
        continue
    trn_lines.add(ln)
    print(ln.split(' ')[0])
    trn_audio_set.add(ln.split(' ')[0])
        
print('audio set length')
print(len(dev_audio_set))
print(len(tst_audio_set))
print(len(trn_audio_set))



fid1 = open('../data/train_asr003/wav.scp','w')
fid2 = open('../data/dev_asr003/wav.scp','w')
fid3 = open('../data/test_asr003/wav.scp','w')

trn_ln_set = set()
dev_ln_set = set()
tst_ln_set = set()
for ln in audio_set:
    print(ln)
    tmp = ln.strip().split(' ')
    recording_id = tmp[0]
    print(recording_id)
    if recording_id in trn_audio_set:
        trn_ln_set.add(ln)
        #fid1.write(ln)                   
    if recording_id in dev_audio_set:
        dev_ln_set.add(ln)
        #fid2.write(ln)
    if recording_id in tst_audio_set:
        tst_ln_set.add(ln)
        #fid3.write(ln)
for ln in sorted(trn_ln_set):
    fid1.write(ln)
fid1.close()
for ln in sorted(dev_ln_set):
    fid2.write(ln)
fid2.close()
for ln in sorted(tst_ln_set):
    fid3.write(ln)
fid3.close()


segment_file = '../data/use_asr003/segments'
fid= open(segment_file)
all_lines = fid.readlines()
fid.close()

fid1 = open('../data/train_asr003/segments','w')
fid2 = open('../data/dev_asr003/segments','w')
fid3 = open('../data/test_asr003/segments','w')

trn_utt_set = set()
dev_utt_set = set()
tst_utt_set = set()

trn_ln_set = set()
dev_ln_set = set()
tst_ln_set = set()

for ln in all_lines:
    if 'None' in ln:
        continue
    tmp = ln.strip().split(' ')
    recording_id = tmp[1]
    utt_id = tmp[0]
    if recording_id in trn_audio_set:
        trn_ln_set.add(ln)
        trn_utt_set.add(utt_id)
    if recording_id in dev_audio_set:
        dev_ln_set.add(ln)
        dev_utt_set.add(utt_id)
    if recording_id in tst_audio_set:
        tst_ln_set.add(ln)
        tst_utt_set.add(utt_id)
for ln in sorted(trn_ln_set):
    fid1.write(ln)
fid1.close()
for ln in sorted(dev_ln_set):
    fid2.write(ln)
fid2.close()
for ln in sorted(tst_ln_set):
    fid3.write(ln)
fid3.close()

print (len(trn_utt_set))
print(len(dev_utt_set))
print(len(tst_utt_set))

text_file = '../data/use_asr003/text'
fid = open(text_file)
all_lines = fid.readlines()
fid.close()



trn_ln_set = set()
dev_ln_set = set()
tst_ln_set = set()

fid1 = open('../data/train_asr003/text','w')
fid2 = open('../data/dev_asr003/text','w')
fid3 = open('../data/test_asr003/text','w')
for ln in all_lines:
    tmp = ln.strip().split(' ')
    utt_id = tmp[0]
    if 'None' in utt_id:
        continue
    if utt_id in trn_utt_set:
        trn_ln_set.add(ln)
    if utt_id in dev_utt_set:
        dev_ln_set.add(ln)
    if utt_id in tst_utt_set:
        tst_ln_set.add(ln)
for ln in sorted(trn_ln_set):
    fid1.write(ln)
fid1.close()
for ln in sorted(dev_ln_set):
    fid2.write(ln)
fid2.close()
for ln in sorted(tst_ln_set):
    fid3.write(ln)
fid3.close()


text_file = '../data/use_asr003/text'
fid = open(text_file)
all_lines = fid.readlines()
fid.close()


fid1 = open('../data/train_asr003/utt2spk','w')
fid2 = open('../data/train_asr003/spk2gender','w')
fid3 = open('../data/dev_asr003/utt2spk','w')
fid4 = open('../data/dev_asr003/spk2gender','w')
fid5 = open('../data/test_asr003/utt2spk','w')
fid6 = open('../data/test_asr003/spk2gender','w')

trn_utt2spk_ln_set = set()
dev_utt2spk_ln_set = set()
tst_utt2spk_ln_set = set()
trn_spk2gender_ln_set = set()
dev_spk2gender_ln_set = set()
tst_spk2gender_ln_set = set()

for ln in all_lines:
    tmp = ln.strip().split(' ')
    utt_id = tmp[0]
    if 'None' in utt_id:
        continue
    spk_id = utt_id.split('spkr')[0]+'spkr'+utt_id.split('spkr')[1][0]
    gender = spk_id[0].lower()
    if utt_id in trn_utt_set:
        trn_utt2spk_ln_set.add(utt_id+' '+spk_id+'\n')
        trn_spk2gender_ln_set.add(spk_id+' '+gender+'\n')
    if utt_id in dev_utt_set:
        dev_utt2spk_ln_set.add(utt_id+' '+spk_id+'\n')
        dev_spk2gender_ln_set.add(spk_id+' '+gender+'\n')
    if utt_id in tst_utt_set:
        tst_utt2spk_ln_set.add(utt_id+' '+spk_id+'\n')
        tst_spk2gender_ln_set.add(spk_id+' '+gender+'\n')
for ln in sorted(trn_utt2spk_ln_set):
    fid1.write(ln)
fid1.close()
for ln in sorted(trn_spk2gender_ln_set):
    fid2.write(ln)
fid2.close()
for ln in sorted(dev_utt2spk_ln_set):
    fid3.write(ln)
fid3.close()
for ln in sorted(dev_spk2gender_ln_set):
    fid4.write(ln)
fid4.close()
for ln in sorted(tst_utt2spk_ln_set):
    fid5.write(ln)
fid5.close()
for ln in sorted(tst_spk2gender_ln_set):
    fid6.write(ln)
fid6.close()
os.system('../utils/utt2spk_to_spk2utt.pl ../data/train_asr003/utt2spk '+'> ../data/train_asr003/spk2utt')
os.system('../utils/utt2spk_to_spk2utt.pl ../data/dev_asr003/utt2spk '+'> ../data/dev_asr003/spk2utt')
os.system('../utils/utt2spk_to_spk2utt.pl ../data/test_asr003/utt2spk '+'> ../data/test_asr003/spk2utt')




