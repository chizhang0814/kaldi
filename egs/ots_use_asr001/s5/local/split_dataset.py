import os
import math
import random 

root_dir = '/data'
content_lst = root_dir+'/USE_ASR001/INDEX/CONTENTS.LST'
fid = open(content_lst)
all_lines = fid.readlines()
fid.close()

print(len(all_lines))
dev_len = int(math.floor(0.1*(len(all_lines)-1)))
tst_len = int(math.floor(0.1*(len(all_lines)-1)))
print(dev_len)

dev_lines = set()
tst_lines = set()
trn_lines = set()

# Randomly select files to add into dev set and test set
for i in range(dev_len):
    idx = random.randint(1, len(all_lines)-1)
    while ((all_lines[idx] in dev_lines) or (all_lines[idx] in tst_lines)):
    	idx = random.randint(1, len(all_lines)-1)
    dev_lines.add(all_lines[idx])

for i in range(tst_len):
    idx = random.randint(1, len(all_lines)-1)
	
    while ((all_lines[idx] in dev_lines) or (all_lines[idx] in tst_lines)):
        idx = random.randint(1, len(all_lines)-1)
    tst_lines.add(all_lines[idx])
# add rest lines into train set
for ln in all_lines[1:]: # skip the first line, which are the column names
    if ((ln in dev_lines) or (ln in tst_lines)):
        continue
    trn_lines.add(ln)

set_dict  = {"train":trn_lines,"dev":dev_lines, "test":tst_lines}

dst_folder = '../data'
if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

corpus = []

for sub in ['train','dev','test']:
    subfolder = dst_folder+'/'+sub
    print(subfolder)
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)	
	
    spkr_set = set()
    sub_lines = set_dict[sub]

    wav_scp = []
    sub_text = []
    utt2spk = []
    for ln in sub_lines:
        if "**" in ln:
            continue
        if "~" in ln:
            continue
        file_text = ln.split('\t')[-1].strip().split(',')[-1].strip()
        if len(file_text)<1:
            continue
        temp = ln.split('\t')
        fname = root_dir+temp[0].replace('\\','/')+'/'+temp[1].split(',')[0].split('.WAV')[0]
        if os.stat(fname).st_size <= 960:
            print(fname)
            continue
        spkr = '_'.join(temp[3:6])
        spkr_set.add(spkr+' '+temp[4].lower())
        
        utt_id = spkr+'_'+temp[0].split('\\')[-1]+'_'+temp[1].split('.')[0]
#        file_path = root_dir+temp[0].replace('\\','/')+'/'+temp[1].split('.')[0]+'.wav'
        file_path = 'sox -t raw -r 48000 -b 16 -e signed-integer '+fname +'  -r 16000 -b 16 -e signed-integer -t wav - |'
        #print(file_path)
        wav_scp.append(utt_id+' '+file_path)

    
        utt2spk.append(utt_id+ ' '+spkr)
        if len(file_text)<1:
            print(ln)
        file_text = file_text.replace('*','').replace('[spk]','').replace('[fil]','').strip().upper()
        corpus.append(file_text)
        sub_text.append(utt_id+' '+file_text)

    fid  = open(dst_folder+'/'+sub+'/spk2gender', 'w')
    for spk in sorted(spkr_set):
        fid.write(spk+'\n')
    fid.close()

    fid = open(dst_folder+'/'+sub+'/wav.scp', 'w')
    for wav in sorted(wav_scp):
        fid.write(wav+'\n')
    fid.close()
	
    fid = open(dst_folder+'/'+sub+'/text', 'w')
    for ln in sorted(sub_text):
        fid.write(ln+'\n')
    fid.close()

    fid = open(dst_folder+'/'+sub+'/utt2spk', 'w')
    for ln in sorted(utt2spk):
        fid.write(ln+'\n')
    fid.close()

#generate corpus data 
if not os.path.exists(dst_folder+'/local'):
    os.mkdir(dst_folder+'/local')

fid = open('../data/local/lm/ots_use_asr001_text.txt', 'w')
for ln in sorted(set(corpus)):
    fid.write(ln+'\n')
fid.close()


