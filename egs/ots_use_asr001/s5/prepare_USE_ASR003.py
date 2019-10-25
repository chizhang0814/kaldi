import os
import glob
import pandas as pd 
import re

demo_file = '/Users/czhang/Downloads/USE_ASR003/Demographics.csv'
transcription_dir = '/Users/czhang/Downloads/USE_ASR003/TRANSCRIPTION_SEGMENTED_TO_SENTENCES'

#tff = open('Utterance_'+language_locale+'.csv', 'w')
#tff.write('Utterance_ID,Gender,Age,Accent,Duration,Spoken_Type,Recording,Locale,Domain,Transcription\n')
print('---------', demo_file)
print('---------', transcription_dir)
demongraph = pd.read_csv(demo_file)
# print(demongraph)
demon_sub = demongraph[['filename','domains-topics','device-type','gender01','gender02','age-group01','age-group02','country-of-residence01','country-of-residence02','country-of-origin01','country-of-origin02']]
   
print(demon_sub)

id_gender = {}
id_age = {}
audio_root = '/'
utterance = pd.DataFrame(columns=['recording-id', 'utterance-id', 'Gender', 'Age', 'Accent', 'Duration','Spoken_Type', 'Recording', 'Locale', 'Domain', 'Transcription'])
count = 0
word_dict = set()
sent_dict = set()

segfid = open('/Users/czhang/Downloads/segments','w')
textfid = open('/Users/czhang/Downloads/text','w')
text_list  = []
seg_list = []
for index, row in demon_sub.iterrows():
    recording_id = row['filename'].split('.')[0]
    audio_file = audio_root+row['filename']
    trans_file = transcription_dir+'/'+row['filename'].split('_')[0]+'/'+recording_id+'.txt'
    if not os.path.exists(trans_file):
        print(trans_file)
    fid = open(trans_file)
    all_lines = fid.readlines()
    fid.close()

    sp1_utt_cnt = 0
    sp2_utt_cnt = 0
    previous_ts = 0.0
    st = []
    spks = row['filename'].split('_')[0]
    #print(spks)
    #print(str(len(spks)))
    #print(str(len(spks)/2+1))
    spkr1 = spks[:int(len(spks)/2)]+'_spkr1'
    spkr2 = spks[int(len(spks)/2):]+'_spkr2'
    #print(spkr1)
    #print(spkr2)
    #print(recording_id)
    
    for ln in all_lines:
        if len(ln.strip()) >0:
            if ln.strip()[0] == '[':
                if len(st) > 0:
                    st_ts = previous_ts
                    ed_ts = float(ln[1:-2].strip())
                    cnt = st
                    #if 'F1054M1054_USA_USA_013' == recording_id:
                    #    print(utter_id)
                    seg_list.append(utter_id+' '+recording_id+' '+str(st_ts)+' '+str(ed_ts)+'\n')
                    #print(seg_list)
                    text_list.append(utter_id+' '+' '.join(wd_list)+'\n')
                    utter_id = ''
                    previous_ts = ed_ts
                else:
                    previous_ts = float(ln[1:-2].strip())
            elif ln.strip()[0] == '<':
                utter_id = ''
                trans = ''
                st = ln.strip()
                temp  = st.replace('<no-speech>', '').replace('<breath>','').replace('<click>','').replace('<sta>', '').replace('<int>','').replace('<breath>','').replace('<overlap>','').replace('<lipsmack>','').replace('<laughter>','').replace('<cough>','').replace('(())','').replace('<hesitation>','').replace(',','').replace('.','').replace('?','').strip()
                if len(temp) ==0:
                #if (st == '<no-speech>') or (st =='<breath>') or (st == '<click>') or(st =='<int>') or (st =='<sta>') or(st =='<int> <no-speech>') or (st == '<no-speech> <int>') or(st == '<int> <breath>') or (st == '<click> <breath>') or (st =='<no-speech> <breath>') or(st =='<sta> <no-speech>') or (st =='<laughter>') or (st =='<lipsmack>') or(st == '<no-speech> <lipsmack> <breath>') or(st == '<no-speech> <click>') or (st == '<click> <no-speech> <breath>') or (st == '<no-speech> <sta>') or (st=='<no-speech> <lipsmack>') or (st == '<click> <no-speech>') or (st == '<no-speech> <int> <no-speech>') or (st == '<lipsmack> <breath>') or (st == '<int> <lipsmack>') or (st == '<no-speech> <laughter>' ) or (st == '<sta> <lipsmack>') or (st == '<sta> <breath>') or (st == '<hesitation> <lipsmack>') or (st == '<cough>') or (st == '<cough> <cough>') or (st == '<sta> <int>') or (st =='<overlap>') or (st == '<sta> <clik>') or (st == '<sta> <no-speech> <sta>') or (st == '<int> <breath> <no-speech>') or (st == '<sta> <cough>') or(st == '<no-speech> <overlap>') or (st == '<int> <click>'):
                    st = []
                    continue
                elif '<Speaker_1' in ln:
                    #if 'F1054M1054_USA_USA_013' == recording_id:
                    #    print(ln)
                    sp1_utt_cnt +=1
                    utter_id = spkr1+'_'+recording_id.split('_')[-1]+'_'+str(sp1_utt_cnt)
                    trans = st.replace('<no-speech>', '').replace('<breath>','').replace('<click>','').replace('<sta>', '').replace('<int>','').replace('<breath>','').replace('<overlap>','').replace('<lipsmack>','').replace('<laughter>','').replace('<cough>','').replace('(())','').replace('<hesitation>','').replace('<Speaker_1>','').strip()
                elif '<Speaker_2'  in ln:
                    sp2_utt_cnt +=1
                    utter_id = spkr2+'_'+recording_id.split('_')[-1]+'_'+str(sp2_utt_cnt)
                    trans = st.replace('<no-speech>', '').replace('<breath>','').replace('<click>','').replace('<sta>', '').replace('<int>','').replace('<breath>','').replace('<overlap>','').replace('<lipsmack>','').replace('<laughter>','').replace('<cough>','').replace('(())','').replace('<hesitation>','').replace('<Speaker_2>','').strip()
                elif '<Speaker_'  in ln:
                    st=[]
                    continue
                elif '<Speaker' not in ln:
                    st = []
                    continue
                #print(trans)
                while '  ' in trans:
                    trans =trans.replace( '  ',' ')
                #print(trans)
                wd_list = []
                for sen in trans.replace('?','.').replace('!','.').split('.'):
                    
                    if len(sen.strip())>0:
                        tmp_sen = sen.replace(',','').replace('.','').replace('--','').strip()
                        while '  ' in tmp_sen:
                            tmp_sen = tmp_sen.replace('  ',' ')
                        #print('sent is:' +tmp_sen.upper())
                        if len(tmp_sen)==0:
                            #print(ln)
                            #print('tmp_sen is:'+tmp_sen)
                            continue
                        #sent_dict.add(tmp_sen.upper().strip())
                        sent_wd_list = []
                        for wd in tmp_sen.split(' '):
                            #print(wd)
                            if wd[-1] == '-':
                                print(wd)
                                continue
                            sent_wd_list.append(wd.strip())
                            word_dict.add(wd.strip())
                            wd_list.append(wd.upper().strip())
                        sent_dict.add((' '.join(sent_wd_list)).upper().strip())
                if len(wd_list) == 0:
                    st = []

                #print(trans)
                #print(' '.join(wd_list))


print(len(sent_dict))
fid = open('/Users/czhang/Downloads/USE_ASR003_train.txt','w')
for sen in sent_dict:
    fid.write(sen+'\n')
fid.close()

fid  = open('/Users/czhang/Downloads/USE_ASR003_words.txt','w')
for wd in sorted(word_dict):
    fid.write(wd+'\n')
fid.close()


for tt in sorted(text_list):
    textfid.write(tt)
textfid.close()

for seg in sorted(seg_list):
    segfid.write(seg)
segfid.close()



                
            
