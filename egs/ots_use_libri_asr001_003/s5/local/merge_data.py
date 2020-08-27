import os

data1 = '../data/train_libri_960_use_asr001'
data2  ='../data/train_asr003'
aim_data = '../data/train_libri_960_use_asr001_asr003'

for ff in ['text', 'segments', 'utt2spk', 'wav.scp']:
    new_set = []
    if os.path.exists(data1+'/'+ff):
        fid = open(data1+'/'+ff)
        all_lines = fid.readlines()
        fid.close()
        for ln in all_lines:
            new_set.append(ln.strip())
    
    all_lines = []
    if os.path.exists(data2+'/'+ff):
        fid = open(data2+'/'+ff)
        all_lines = fid.readlines()
        fid.close()
        for ln in all_lines:
            new_set.append(ln.strip())
    if len(new_set) > 0:
        fid = open(aim_data+'/'+ff,'w')
        for ln in sorted(new_set):
            fid.write(ln+'\n')
        fid.close()


os.system('../utils/utt2spk_to_spk2utt.pl '+aim_data+'/utt2spk > '+aim_data+'/spk2utt')

