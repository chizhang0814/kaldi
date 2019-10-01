import os
import math
import random 

content_lst = '/data/USE_ASR001/USE_ASR001/INDEX/CONTENTS.LST'
fid = open(content_lst)
all_lines = fid.readlines()
fid.close()


dev_len = math.floor(0.1*(len(all_lines)-1))
tst_len = math.floor(0.1*(len(all_lines)-1))


dev_lines = set()
tst_lines = set()
trn_lines = set()

# Randomly select files to add into dev set and test set
for i in range(dev_len):
	idx = random.randint(1, len(all_lines))
	while ((all_lines[idx] in dev_lines) or (all_lines[idx] in tst_lines)):
		idx = random.randint(1, len(all_lines))
	dev_lines.add(all_lines[idx])

for i in range(tst_len):
	idx = random.randint(1, len(all_lines))
	
	while ((all_lines[idx] in dev_lines) or (all_lines[idx] in tst_lines)):
		idx = random.randint(1, len(all_lines))
	tst_lines.add(all_lines[idx])
# add rest lines into train set
for ln in all_lines[1:-1]:
	if ((ln in dev_lines) or (ln in tst_lines)):
		continue
	trn_lines.add(ln)

print(len(tst_lines))
print(len(dev_lines))
print(len(trn_lines))
