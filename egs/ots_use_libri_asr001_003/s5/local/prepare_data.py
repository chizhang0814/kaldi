import os

text_file = 'text'
fid = open(text_file)
all_lines = fid.readlines()
fid.close()

fid1 = open('utt2spk','w')
fid2 = open('spk2gender','w')
for ln in all_lines:
    tmp = ln.strip().split(' ')
    utt_id = tmp[0]
    spk_id = utt_id.split('spkr')[0]+'spkr'+utt_id.split('spkr')[1][0]
    gender = spk_id[0].lower()
    fid1.write(utt_id+' '+spk_id+'\n')
    fid2.write(spk_id+' '+gender+'\n')

fid1.close()
fid2.close()

segment_file = 'segments'
fid= open(segment_file)
all_lines = fid.readlines()
fid.close()

fid3 = open('wav.scp','w')

audio_root = '/data2/USE_ASR003/AUDIO'

for ln in all_lines:
    tmp = ln.strip().split(' ')
    recording_id = tmp[1]
    recording_file = audio_root+'/'+recording_id.split('_')[0]+'/'+recording_id+'.wav'
    
    if not os.path.exists(recording_file):
        print(recording_file)
    fid3.write(recording_id+' '+recording_file+'\n')
fid3.close()

