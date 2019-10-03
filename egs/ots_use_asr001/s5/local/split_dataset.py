import os
import math
import random 

root_dir = '/data/USE_ASR001'
content_lst = '/data/USE_ASR001/USE_ASR001/INDEX/CONTENTS.LST'
fid = open(content_lst)
all_lines = fid.readlines()
fid.close()

print(len(all_lines))
dev_len = math.floor(0.1*(len(all_lines)-1))
tst_len = math.floor(0.1*(len(all_lines)-1))
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
		temp = ln.split('\t')
		spkr = '_'.join(temp[3:6])
		spkr_set.add(spkr+' '+temp[4].lower())
		
		utt_id = temp[0].split('\\')[-1]+'_'+temp[1].split('.')[0]
		file_path = root_dir+temp[0].replace('\\','/')+'/'+temp[1].split('.')[0]+'.wav'
		wav_scp.append(utt_id+' '+file_path)		
		file_text = temp[-1].split(',')[-1].strip()
		sub_text.append(utt_id+' '+file_text)
		utt2spk.append(utt_id+ ' '+spkr)
		corpus.append(file_text)

	fid  = open(dst_folder+'/'+sub+'/spk2gender', 'w')
	for spk in spkr_set:
		fid.write(spk+'\n')
	fid.close()

	fid = open(dst_folder+'/'+sub+'/wav.scp', 'w')
	for wav in wav_scp:
		fid.write(wav+'\n')
	fid.close()
	
	fid = open(dst_folder+'/'+sub+'/text', 'w')
	for ln in sub_text:
		fid.write(ln+'\n')
	fid.close()

	fid = open(dst_folder+'/'+sub+'/utt2spk', 'w')
	for ln in utt2spk:
		fid.write(ln+'\n')
	fid.close()

fid = open('../data/local/corpus.txt', 'w')
for ln in corpus:
	fid.write(ln+'\n')
fid.close()


aa = []
aa.append('123')
print(aa)
aa.append('234')
print(aa)
