import os

input_wav_scp = '/data3/ots_uke_asr001/s5/data/test_appen/wav.scp_bak'
output_wav_scp = '/data3/ots_uke_asr001/s5/data/test_appen/wav.scp'
#sox -t raw -r 48000 -b 16 -e signed-integer /data2/USE_ASR001/BLOCK00/SES001/AP001BA01.UE0  -r 16000 -b 16 -e signed-integer -t wav - |

all_lines = open(input_wav_scp).readlines()
fid = open(output_wav_scp,'w')
for ln in all_lines:
    wav_id, wav_file = ln.split(' ')
    wav_convert = 'sox '+wav_file.strip()+' -r 8000 -b 16 -e signed-integer -t wav - |'
    new_ln = wav_id.strip()+' '+wav_convert
    fid.write(new_ln+'\n')
fid.close()
