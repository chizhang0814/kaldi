import os
import librosa
import soundfile as sf
import glob

root_dir = '/data/USE_ASR001'
content_lst = '/data/USE_ASR001/USE_ASR001/INDEX/CONTENTS.LST'

fid = open(content_lst)
all_lines = fid.readlines()
fid.close()

for ln in all_lines[1:]:
    origin_file = root_dir+ln.split('\t')[0].replace('\\','/')+'/'+ln.split('\t')[1].split(',')[0]
    print(origin_file)
