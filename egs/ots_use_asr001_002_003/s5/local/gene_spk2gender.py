import os 

src_file = '/data/USE_ASR001/USE_ASR001/TABLE/SPEAKER.TBL'
dst_fiel = '../data/spk2gender'
	
fid = open(src_file)
all_lines = fid.readlines()
fid.close()


fid = open(dst_file, 'w')
for ln in all_lines[1:-1]:
	fid.write(ln.split('\t')[0]+' '+ln.split('\t')[1].lower()+'\n')
end

fid.close()
